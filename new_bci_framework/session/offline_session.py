from typing import Iterable, Sequence

import mne.io.fiff

from .session import Session
from ..recorder.recorder import Recorder
from ..classifier.base_classifier import BaseClassifier
from ..paradigm.paradigm import Paradigm
from ..preprocessing.preprocessing_pipeline import PreprocessingPipeline
from ..config.config import Config


class OfflineSession(Session):
    """
    Subclass of session for an offline recording session.
    """

    def __init__(self, recorder: Recorder, paradigm: Paradigm, preprocessor: PreprocessingPipeline,
                 classifier: BaseClassifier, config: Config):
        super().__init__(recorder, paradigm, preprocessor, classifier, config)

    def run_recording(self):
        th = None
        self.recorder.start_recording()
        if self.config.SHOW_LIVE_DATA:
            th = self.recorder.plot_live_data(block=self.config.LIVE_DATA_SHOULD_BLOCK)
        self.paradigm.start(self.recorder)
        if th is not None:
            print("Close live-data window to end recording and continue...")
            th.join()
        self.recorder.end_recording()

    def run_preprocessing(self):
        self.raw_data: mne.io.RawArray = self.recorder.get_raw_data()
        self.epoched_data = self.preprocessor.run_pipeline(self.raw_data)

    def run_classifier(self):
        self.classifier.run(self.epoched_data)

    def run_all(self):
        self.run_recording()
        self.run_preprocessing()
        self.run_classifier()
        self.save_session()

    def load_from_fif(self, fname):
        self.raw_data: mne.io.Raw = mne.io.fiff.read_raw_fif(fname)
        self.raw_data.load_data()
        self.epoched_data = self.preprocessor.run_pipeline(self.raw_data)

    @staticmethod
    def concat_sessions(ses_list: Sequence['OfflineSession']):
        ses_1 = ses_list[0]
        new_ses = OfflineSession(recorder=ses_1.recorder, paradigm=ses_1.paradigm, preprocessor=ses_1.preprocessor, classifier=ses_1.classifier, config=ses_1.config)
        new_raw = mne.concatenate_raws([ses.raw_data for ses in ses_list])
        new_ses.raw_data = new_raw
        new_ses.epoched_data = new_ses.preprocessor.run_pipeline(new_raw)
        return new_ses


