import brainflow
import numpy as np
import pyqtgraph as pg
from brainflow.board_shim import BoardShim, BrainFlowError
from brainflow.data_filter import DataFilter, FilterTypes, DetrendOperations
from pyqtgraph import ViewBox, intColor
from pyqtgraph.Qt import QtGui, QtCore


class Graph:
    def __init__(self, board_shim, ch_names, config):
        self.board_id = board_shim.get_board_id()
        self.board_shim = board_shim
        self.exg_channels = BoardShim.get_exg_channels(self.board_id)
        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)
        self.update_speed_ms = 50
        self.window_size = 5
        self.num_points = self.window_size * self.sampling_rate
        self.ch_names = ch_names
        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title='BrainFlow Plot', size=(800, 600))
        self.config = config
        self._init_timeseries()
        self.prev_amp = np.zeros(129)
        self.__enable_filters = True
        time_series_timer = QtCore.QTimer()
        time_series_timer.timeout.connect(self.update_timeseries)
        time_series_timer.start(self.update_speed_ms)

        psd_update_speed_ms = 100

        psd_timer = QtCore.QTimer()
        psd_timer.timeout.connect(self.update_psd)
        psd_timer.start(psd_update_speed_ms)

        QtGui.QApplication.instance().exec_()

    def _init_timeseries(self):
        self.plots = list()
        self.curves = list()
        self.psd_curves = list()
        self.psd = self.win.addPlot(row=1, col=2, rowspan=len(self.exg_channels)-1)
        # self.control_layout = self.win.addPlot(row=0, colspan=2)
        self.psd.setTitle('Power Spectrum')
        self.psd.setLogMode(y=True)
        self.psd.disableAutoRange(ViewBox.YAxis)
        self.psd.setRange(yRange=(0, 2), xRange=(0, 70))
        self.psd.addLegend((-20, 10))
        self.filter_button = pg.QtGui.QPushButton("Disable Filters")

        proxy = QtGui.QGraphicsProxyWidget()
        proxy.setWidget(self.filter_button)
        self.win.addItem(proxy, col=1)

        def toggle_filters():
            self.__enable_filters = not self.__enable_filters
            self.filter_button.setText(f"{'Disable' if self.__enable_filters else 'Enable'} Filters")

        self.filter_button.clicked.connect(toggle_filters)

        for i in self.config.REAL_CHANNEL_INDXS:
            p = self.win.addPlot(row=i, col=0)
            p.showAxis('left', True)
            p.setLabel('left', self.ch_names[i], 'uV')
            p.setMenuEnabled('left', False)
            p.showAxis('bottom', False)
            p.setMenuEnabled('bottom', False)
            p.disableAutoRange(ViewBox.YAxis)
            p.setRange(yRange=(-50, 50))
            if i == 0:
                p.setTitle('TimeSeries Plot')
            self.plots.append(p)
            color = intColor(i*3 + (i%9),  values=2, sat=200+(2*i))
            curve = p.plot(pen=color, name=self.ch_names[i])
            self.curves.append(curve)
            curve = self.psd.plot(connect='all', pen=color, name=self.ch_names[i])
            self.psd_curves.append(curve)

    def update_timeseries(self):
        data = self.board_shim.get_current_board_data(self.num_points)
        data *= (24 // self.config.GAIN_VALUE)
        for count, channel in enumerate(self.exg_channels[:len(list(self.config.REAL_CHANNEL_INDXS))]):
            # plot timeseries
            if self.__enable_filters:
                DataFilter.detrend(data[channel], DetrendOperations.CONSTANT.value)
                DataFilter.perform_highpass(data[channel], self.sampling_rate, 1, 2,
                                            FilterTypes.BUTTERWORTH.value, 0)
                DataFilter.perform_lowpass(data[channel], self.sampling_rate, 50, 2,
                                           FilterTypes.BUTTERWORTH.value, 0)
                # DataFilter.perform_bandpass(data[channel], self.sampling_rate, 51.0, 100.0, 2,
                #                             FilterTypes.BUTTERWORTH.value, 0)
                # DataFilter.perform_bandpass(data[channel], self.sampling_rate, 51.0, 100.0, 2,
                #                             FilterTypes.BUTTERWORTH.value, 0)
                DataFilter.perform_bandstop(data[channel], self.sampling_rate, 50.0, 4.0, 2,
                                            FilterTypes.BUTTERWORTH.value, 0)
                # DataFilter.perform_bandstop(data[channel], self.sampling_rate, 60.0, 4.0, 2,
                #                             FilterTypes.BUTTERWORTH.value, 0)
            self.curves[count].setData(data[channel].tolist())
        self.app.processEvents()

    def update_psd(self):
        data = self.board_shim.get_current_board_data(256)

        data *= (24 // self.config.GAIN_VALUE)
        for count, channel in enumerate(self.exg_channels[:len(list(self.config.REAL_CHANNEL_INDXS))]):
            # plot timeseries
            if self.__enable_filters:
                DataFilter.detrend(data[channel], DetrendOperations.CONSTANT.value)
                DataFilter.perform_highpass(data[channel], self.sampling_rate, 1, 2,
                                            FilterTypes.BUTTERWORTH.value, 0)
                DataFilter.perform_lowpass(data[channel], self.sampling_rate, 50, 2,
                                           FilterTypes.BUTTERWORTH.value, 0)
                # DataFilter.perform_bandpass(data[channel], self.sampling_rate, 51.0, 100.0, 2,
                #                             FilterTypes.BUTTERWORTH.value, 0)
                # DataFilter.perform_bandpass(data[channel], self.sampling_rate, 51.0, 100.0, 2,
                #                             FilterTypes.BUTTERWORTH.value, 0)
                DataFilter.perform_bandstop(data[channel], self.sampling_rate, 50.0, 4.0, 2,
                                            FilterTypes.BUTTERWORTH.value, 0)
                # DataFilter.perform_bandstop(data[channel], self.sampling_rate, 60.0, 4.0, 2,
                #                             FilterTypes.BUTTERWORTH.value, 0)
            try:
                amp, freq = DataFilter.get_psd(data[channel][-256:], self.sampling_rate,
                                               brainflow.WindowFunctions.HAMMING.value)
            except BrainFlowError:
                # When the data starts arriving there arent 512 points to do fft so get_psd will raise an error.
                freq = np.arange(0, 125)
                amp = np.zeros_like(freq)
                self.prev_amp = amp
            self.prev_amp = self.prev_amp * 0.9 + amp * 0.1
            self.psd_curves[count].setData(freq[:60].tolist(), self.prev_amp[:60].tolist())
        self.app.processEvents()
