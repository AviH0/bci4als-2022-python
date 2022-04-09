import datetime
import os.path
import sys
from typing import Dict

from matplotlib import pyplot as plt


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
        self.SESSION_SAVE_DIR = f"{root_dir}/Session_{self.DATE}_{self.SUBJECT_NAME}"

        if not os.path.isdir(root_dir):
            os.mkdir(root_dir)
        if not os.path.isdir(self.SESSION_SAVE_DIR):
            os.mkdir(self.SESSION_SAVE_DIR)


        # Recorder settings:
        self.MONTAGE_FILENAME = os.path.join(__file__, "..", "..", "recorder", "montage_ultracortex.loc")
        self.SHOW_LIVE_DATA = show_live_data
        if self.__is_macos():
            live_data_should_block = True  # Macos doesn't support GUI manipulation on non-main threads.
        self.LIVE_DATA_SHOULD_BLOCK = live_data_should_block
        self.GAIN_VALUE = 6

        self.SHOW_PLOTS = show_plots

        # This needs to be an dict where the keys are stim values and the values are their labels
        self.TRIAL_LABELS: Dict[int, str] = dict()
        # Set trial start and end times in seconds relative to stimulus (for example -0.2, 0.9)
        self.TRIAL_START_TIME = -0.1
        self.TRIAL_END_TIME = 0.5

        self.MIN_TARGET_APPEARANCES = 2

        # PREPROCESSING:
        self.HIGH_PASS_FILTER = 0.5
        self.LOW_PASS_FILTER = 40
        self.NOTCH_FILTER = 50

    def __is_macos(self):
        return sys.platform.startswith('darwin')