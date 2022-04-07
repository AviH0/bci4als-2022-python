import os
import pickle
from pickle import Pickler

from ..recorder.recorder import Recorder
from ..classifier.base_classifier import BaseClassifier
from ..paradigm.paradigm import Paradigm
from ..preprocessing.preprocessing_pipeline import PreprocessingPipeline
from ..config.config import Config

SESSION_SAVE_FILE_PICKLE = "session_save_file.pickle"


class Session:
    """
    Base class for an EEG session, with online or offline recording, or analysis of previous recordings.
    simple public api for creating and running the session.
    """

    def __init__(self, recorder: Recorder, paradigm: Paradigm, preprocessor: PreprocessingPipeline,
                 classifier: BaseClassifier, config: Config):
        self.recorder = recorder
        self.paradigm = paradigm
        self.preprocessor = preprocessor
        self.classifier = classifier
        self.config = config
        self.raw_data = None
        self.epoched_data = None

    def run_all(self):
        raise NotImplementedError

    def save_session(self):
        with open(os.path.join(self.config.SESSION_SAVE_DIR, SESSION_SAVE_FILE_PICKLE), 'wb') as savefile:
            Pickler(savefile).dump(self)

    @staticmethod
    def load_session(session_dir: str):
        """
        Load a previously recorded session from disk to preform analysis.
        :param session_dir: saved session directory
        :return: Session object
        """
        with open(os.path.join(session_dir, SESSION_SAVE_FILE_PICKLE), 'rb') as savefile:
            return pickle.load(savefile)