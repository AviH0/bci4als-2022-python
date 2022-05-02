import atexit
import threading
import time
from typing import Optional, List, Union

import matplotlib.pyplot as plt
import mne
import numpy as np
from mne.io import RawArray
from nptyping import NDArray

from .plot_rt_recording import Graph
from .recorder import Recorder
import serial.tools.list_ports
from brainflow import BrainFlowInputParams, BoardShim, BoardIds

from ..config.config import Config


class CytonRecorder(Recorder):



    def __init__(self, config: Config,
                 board_id: int = BoardIds.CYTON_DAISY_BOARD.value,
                 ip_port: int = 6677,
                 serial_port: Optional[str] = None,
                 headset: str = "cyton",
                 synthetic_data=False):
        super(CytonRecorder, self).__init__(config)
        if synthetic_data:
            board_id = BoardIds.SYNTHETIC_BOARD
        self._config = config
        self.__seen_markers = 0
        self.headset: str = headset
        self.board_id = board_id
        self.__is_recording = False
        # Board Id and Headset Name

        # synthetic headset name
        if board_id == BoardIds.SYNTHETIC_BOARD:
            self.headset = 'synth'

        # BrainFlowInputParams
        self.params = BrainFlowInputParams()
        self.params.ip_port = ip_port
        self.params.serial_port = serial_port if serial_port is not None else self.__find_serial_port()
        self.params.headset = headset
        self.params.board_id = board_id
        self.board = BoardShim(board_id, self.params)

        # Other Params
        self.sfreq = self.board.get_sampling_rate(board_id)
        self.marker_row = self.board.get_marker_channel(self.board_id)
        self.eeg_names = self.__get_board_names()
        self.data = None

    def start_recording(self):
        self.__on()

    def push_marker(self, marker):
        if not marker:
            # zero is default value so do nothing
            return
        if marker not in self._config.TRIAL_LABELS:
            self.__seen_markers += 1
            self._config.TRIAL_LABELS[marker] = f"Stimulus_{self.__seen_markers}"
        self.__insert_marker(marker)

    def end_recording(self):
        self.__off()

    def get_raw_data(self) -> RawArray:
        return self.__get_raw_data(self.__get_board_names())

    def get_live_capture(self) -> RawArray:
        return self.__get_raw_data(self.__get_board_names(), full=False)

    def plot_live_data(self, block=True) -> Union[None, threading.Thread]:
        start_plot = lambda: Graph(self.board, self.__get_board_names())
        if block:
            start_plot()
        else:
            thread = threading.Thread(target=start_plot)
            thread.start()
            return thread


    def __find_serial_port(self) -> str:
        """
        Return the string of the serial port to which the FTDI dongle is connected.
        If running in Synthetic mode, return ""
        Example: return "COM5"
        """
        if self.board_id == BoardIds.SYNTHETIC_BOARD:
            return ""
        else:
            plist = serial.tools.list_ports.comports()
            FTDIlist = [comport for comport in plist if comport.manufacturer == 'FTDI']
            if len(FTDIlist) > 1:
                raise LookupError(
                    "More than one FTDI-manufactured device is connected. Please enter serial_port manually.")
            if len(FTDIlist) < 1:
                raise LookupError("FTDI-manufactured device not found. Please check the dongle is connected")
            return FTDIlist[0].name

    def __get_board_names(self) -> List[str]:
        """The method returns the board's channels"""
        if self.headset == "cyton":
            return self._config.CYTON_CHANNEL_NAMES
        else:
            return self.board.get_eeg_names(self.board_id)

    def __channel_hardware_settings(self, channel_index, gain_setting=3, power_on=True):
        CHANNELS = "12345678QWERTYUI"
        chan = CHANNELS[channel_index]
        power = 0 if power_on else 1
        input_type = 0 if power_on else 1
        bias = 1 if power_on else 0
        srb2 = 1 if power_on else 0
        srb1 = 0
        self.board.config_board(f"x{chan}{power}{gain_setting}{input_type}{bias}{srb2}{srb1}X")

    def __on(self):
        """Turn EEG On"""
        self.__is_recording = True
        self.board.prepare_session()

        if self.board_id == BoardIds.CYTON_DAISY_BOARD:
            # According to https://docs.openbci.com/Cyton/CytonSDK/#channel-setting-commands
            GAIN_VALUE_TO_SETTING = {1: 0, 2: 1, 4: 2, 6: 3, 8: 4, 12: 5, 24: 6}

            for i in self._config.REAL_CHANNEL_INDXS:
                self.__channel_hardware_settings(i, gain_setting=GAIN_VALUE_TO_SETTING[self._config.GAIN_VALUE])
            for i in self._config.BAD_CHANNEL_INDXS:
                self.__channel_hardware_settings(i, power_on=False)
        self.board.start_stream()

    def __off(self):
        """Turn EEG Off"""
        self.__get_board_data()
        self.__is_recording = False
        self.board.stop_stream()
        self.board.release_session()

    def __insert_marker(self, marker: float):
        """Insert an encoded marker into EEG data"""

        # marker = self.encode_marker(status, label, index)  # encode marker
        self.board.insert_marker(marker)  # insert the marker to the stream

        # print(f'Status: { status }, Marker: { marker }')  # debug
        # print(f'Count: { self.board.get_board_data_count() }')  # debug

    def __board_to_mne(self, board_data: NDArray, stim: NDArray, ch_names: List[str]) -> mne.io.RawArray:
        """
        Convert the ndarray board data to mne object
        :param board_data: raw ndarray from board
        :return:
        """
        eeg_data = board_data / 1000000  # BrainFlow returns uV, convert to V for MNE


        if self.board_id == BoardIds.CYTON_DAISY_BOARD:
            # rescale if gain value is not 24:
            eeg_data *= (24 // self._config.GAIN_VALUE)  # calculation for 24 is here: https://github.com/brainflow-dev/brainflow/blob/master/src/board_controller/openbci/inc/cyton_daisy.h

        # Add marker channel:
        # eeg_data = np.stack([eeg_data, self.board.get_marker_channel(self.board_id)])
        marker_info = mne.create_info(ch_names=['stim'], sfreq=self.sfreq, ch_types=['stim'])
        marker_raw = mne.io.RawArray([stim], marker_info)
        event_dict = {v: k for k, v in self._config.TRIAL_LABELS.items()}
        events = mne.find_events(marker_raw, stim_channel="stim", output="onset")
        if events is not None:
            fig = mne.viz.plot_events(events, show=False, event_id=event_dict, sfreq=self.sfreq)
            fig.savefig(f"{self._data_dir}/events.png")
        if self._config.SHOW_PLOTS:
            plt.show(block=False)
        # Creating MNE objects from BrainFlow data arrays
        ch_types = ['eeg'] * len(board_data)
        info = mne.create_info(ch_names=ch_names, sfreq=self.sfreq, ch_types=ch_types)
        if self.board_id == BoardIds.CYTON_DAISY_BOARD:
            montage = mne.channels.read_custom_montage(fname=self._config.MONTAGE_FILENAME)
        else:
            montage = mne.channels.make_standard_montage('biosemi64')
        info.set_montage(montage)
        raw = mne.io.RawArray(eeg_data, info, verbose=False)
        raw.add_channels([marker_raw])
        drop_channels = [name for index, name in enumerate(ch_names) if index in self._config.BAD_CHANNEL_INDXS]
        return raw.drop_channels(drop_channels)

    def __get_board_data(self) -> NDArray:
        """The method returns the current data from board, removes it from the buffer and adds it to static
         storage"""
        if self.__is_recording:
            new_data = self.board.get_board_data()
            if self.data is None:
                self.data = new_data
            else:
                np.concatenate([self.data, new_data], axis=1)
            return new_data
        return self.data

    def __get_raw_data(self, ch_names: List[str], full=True) -> mne.io.RawArray:
        """
        The method returns dataframe with all the raw data, and empties the buffer
        :param ch_names: list[str] of channels to select
        :return: mne_raw data
        """

        indices = [self.eeg_names.index(ch) + 1 for ch in ch_names]

        if full:
            self.__get_board_data()
            data = self.data
        else:
            data = self.__get_board_data()

        stim = data[self.board.get_marker_channel(self.board_id)]
        data = data[indices]
        return self.__board_to_mne(data, stim, ch_names)
