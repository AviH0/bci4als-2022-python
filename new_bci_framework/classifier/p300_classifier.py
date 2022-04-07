import mne

from new_bci_framework.classifier.base_classifier import BaseClassifier
from new_bci_framework.config.config import Config


class P300Classifier(BaseClassifier):

    def __init__(self, config: Config):
        super().__init__(config)

    def fit(self, data=mne.Epochs):
        event_dict = {v: k for k, v in self._config.TRIAL_LABELS.items()}

    def predict(self, data: mne.Epochs):
        pass

    def evaluate(self, data: mne.Epochs):
        pass

    def train_test_split(self, data: mne.Epochs):
        return None, None
