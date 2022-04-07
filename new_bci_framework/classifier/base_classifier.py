import mne
from ..config.config import Config


class BaseClassifier:
    """
    Basic class for a classifier for session eeg data.
    API includes training, prediction and evaluation.
    """

    def __init__(self, config: Config):
        self._config = config

    def fit(self, data=mne.Epochs):
        raise NotImplementedError

    def train_test_split(self, data: mne.Epochs):
        raise NotImplementedError

    def predict(self, data: mne.Epochs):
        raise NotImplementedError

    def evaluate(self, data: mne.Epochs):
        raise NotImplementedError
