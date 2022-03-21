import datetime


class Config:
    """
    class containing config information for a session.
    This should include any configurable parameters of all the other classes, such as
    directory names for saved data and figures, numbers of trials, train-test-split ratio, etc.
    """

    SUBJECT_NAME = ""
    DATE = datetime.datetime.now().date().isoformat()
    SESSION_SAVE_DIR = f"Session_{DATE}_{SUBJECT_NAME}"

    # This needs to be an dict where the keys are stim values and the values are their labels
    TRIAL_LABELS = dict()
    # Set trial start and end times in seconds relative to stimulus (for example -0.2, 0.9)
    TRIAL_START_TIME = 0.0
    TRIAL_END_TIME = 0.0

    #PREPROCESSING:
    HIGH_PASS_FILTER = 0.1
    LOW_PASS_FILTER = 40
    NOTCH_FILTER = 50

