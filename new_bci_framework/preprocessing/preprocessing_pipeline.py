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
        self.__config = config
        self.__data_dir = self.__config.SESSION_SAVE_DIR

    def __segement(self, data: mne.io.Raw) -> mne.Epochs:
        event_dict = {v: k for k, v in self.__config.TRIAL_LABELS.items()}
        events = mne.find_events(data, output="onset", shortest_event=0)

        epochs = mne.Epochs(data,
                            events,
                            tmin=self.__config.TRIAL_START_TIME,
                            tmax=self.__config.TRIAL_END_TIME,
                            event_id=event_dict,
                            verbose='INFO',
                            on_missing='warn')
        return epochs

    def __filter(self,  data: mne.io.Raw) -> None:
        data.filter(l_freq=self.__config.LOW_PASS_FILTER, h_freq=self.__config.HIGH_PASS_FILTER)
        if self.__config.NOTCH_FILTER:
            data.notch_filter(self.__config.NOTCH_FILTER)

    def run_pipeline(self, data: mne.io.Raw) -> mne.Epochs:
        self.__filter(data)
        return self.__segement(data)
