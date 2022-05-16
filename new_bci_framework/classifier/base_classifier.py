import mne
from ..config.config import Config


class BaseClassifier:
    """
    Basic class for a classifier for session eeg data.
    API includes training, prediction and evaluation.
    """

    def __init__(self, config: Config):
        self._config = config

    def run(self, data: mne.Epochs):
        raise NotImplementedError


