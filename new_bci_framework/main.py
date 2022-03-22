from new_bci_framework.paradigm.dummy_paradigm import DummyParadigm
from new_bci_framework.preprocessing.p300_preprocessing import P300Preprocessing
from new_bci_framework.recorder.opeb_bci_cyton_recorder import CytonRecorder
from new_bci_framework.recorder.test import main_test
from new_bci_framework.classifier.base_classifier import BaseClassifier
from new_bci_framework.config.config import Config
from new_bci_framework.paradigm.p300_paradigm import P300Paradaigm
from new_bci_framework.preprocessing.preprocessing_pipeline import PreprocessingPipeline
from new_bci_framework.recorder.recorder import Recorder
from new_bci_framework.session.offline_session import OfflineSession
from new_bci_framework.session.session import Session

if __name__ == '__main__':

    subject_name = input("input subject name")
    kwargs = {'root_dir': '../sessions'}
    if subject_name:
        kwargs['subject_name'] = subject_name
    config = Config(**kwargs)

    session = OfflineSession(
        recorder=CytonRecorder(config, synthetic_data=True),
        paradigm=DummyParadigm(config),
        preprocessor=P300Preprocessing(config),
        classifier=BaseClassifier(config),
        config=config
    )
    session.run_all()
    # main_test()