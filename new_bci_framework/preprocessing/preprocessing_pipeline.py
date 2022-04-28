import os
from typing import Dict

import mne

from ..config.config import Config


class PreprocessingPipeline:
    """
    A Preprocessing pipeline. In essence it receives a raw data object and returns teh segmented data as
    an Epochs object, after preforming filters, cleaning etc.
    Further design of this class can allow subclassing or other forms of modularity, allowing us to easily
    swap different pipelines.
    """

    def __init__(self, config: Config):
        self._config = config
        self.__original_data = None
        self._save_dir = f"{self._config.SESSION_SAVE_DIR}/preprocessor"
        if not os.path.isdir(self._save_dir):
            os.mkdir(self._save_dir)

    def __segement(self, data: mne.io.Raw) -> mne.Epochs:
        event_dict: Dict[str, int] = {v: k for k, v in self._config.TRIAL_LABELS.items()}
        events = mne.find_events(data, output="onset")

        epochs = mne.Epochs(data,
                            events,
                            tmin=self._config.TRIAL_START_TIME,
                            tmax=self._config.TRIAL_END_TIME,
                            event_id=event_dict,
                            verbose='INFO',
                            on_missing='warn')
        return epochs

    def __filter(self,  data: mne.io.Raw) -> None:
        self.__original_data = data.copy()
        data.save(os.path.join(self._save_dir, "original_raw.fif"), overwrite=True)
        data.filter(l_freq=self._config.HIGH_PASS_FILTER, h_freq=self._config.LOW_PASS_FILTER)
        if self._config.NOTCH_FILTER:
            data.notch_filter(self._config.NOTCH_FILTER)

    def run_pipeline(self, data: mne.io.Raw) -> mne.Epochs:
        self.__filter(data)
        return self.__segement(data)
