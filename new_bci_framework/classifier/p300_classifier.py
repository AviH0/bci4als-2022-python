import mne

from new_bci_framework.classifier.base_classifier import BaseClassifier
from new_bci_framework.config.config import Config


class P300Classifier(BaseClassifier):

    def __init__(self, config: Config):
        super().__init__(config)

    def fit(self, data=mne.Epochs):
        event_dict = {v: k for k, v in self.__config.TRIAL_LABELS.items()}

        super().fit(data)

    def predict(self, data: mne.Epochs):
        super().predict(data)

    def evaluate(self, data: mne.Epochs):
        super().evaluate(data)