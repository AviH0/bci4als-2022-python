import datetime
import os.path
import sys
from typing import Dict

from matplotlib import pyplot as plt

from new_bci_framework.logging.file_logger import FileLogger


class Config:
    """
    class containing config information for a session.
    This should include any configurable parameters of all the other classes, such as
    directory names for saved data and figures, numbers of trials, train-test-split ratio, etc.
    """

    def __init__(self,
                 subject_name="TEST_SUBJECT",
                 show_plots=False,
                 show_live_data=True,
                 root_dir=".",
                 live_data_should_block=False,
                 matplotlib_backend='QtAgg'
                 ):

        plt.switch_backend(matplotlib_backend)


        self.SUBJECT_NAME = subject_name
        self.DATE = datetime.datetime.now().date().isoformat()
        base_session_dir = f"{root_dir}/Session_{self.DATE}_{self.SUBJECT_NAME}"
        subject_count = 1
        self.SESSION_SAVE_DIR = f"{base_session_dir}-{subject_count}"

        if not os.path.isdir(root_dir):
            os.mkdir(root_dir)
        while os.path.isdir(self.SESSION_SAVE_DIR):
            subject_count += 1
            self.SESSION_SAVE_DIR = f"{base_session_dir}-{subject_count}"
        os.mkdir(self.SESSION_SAVE_DIR)

        self.LOG_FILE_PATH = os.path.join(self.SESSION_SAVE_DIR, "log.txt")
        self.logger = FileLogger(self.LOG_FILE_PATH)

        # Recorder settings:
        self.MONTAGE_FILENAME = os.path.join(__file__, "..", "..", "recorder", "montage_ultracortex.loc")
        self.SHOW_LIVE_DATA = show_live_data
        if self.__is_macos():
            live_data_should_block = True  # Macos doesn't support GUI manipulation on non-main threads.
        self.LIVE_DATA_SHOULD_BLOCK = live_data_should_block
        self.GAIN_VALUE = 6
        self.CYTON_CHANNEL_NAMES = ['C3', 'C4', 'Cz', 'FC1', 'FC2', 'FC5', 'FC6', 'CP1', 'CP2', 'CP5', 'CP6', 'O1', 'O2', 'T8', 'PO3', 'PO4']
        self.REAL_CHANNEL_INDXS = range(13)
        self.BAD_CHANNEL_INDXS = range(13, 16)
        self.SHOW_PLOTS = show_plots

        # This needs to be an dict where the keys are stim values and the values are their labels
        self.TRIAL_LABELS: Dict[float, str] = dict()
        # Set trial start and end times in seconds relative to stimulus (for example -0.2, 0.9)
        self.TRIAL_START_TIME = -0.2
        self.TRIAL_END_TIME = 1.1

        self.MIN_TARGET_APPEARANCES = 2

        # PREPROCESSING:
        self.HIGH_PASS_FILTER = 0.5
        self.LOW_PASS_FILTER = 40
        self.NOTCH_FILTER = 50

    def __is_macos(self):
        return sys.platform.startswith('darwin')