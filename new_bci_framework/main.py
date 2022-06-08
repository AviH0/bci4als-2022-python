import os

from new_bci_framework.classifier.p300_classifier import P300Classifier
from new_bci_framework.paradigm.dummy_paradigm import DummyParadigm
from new_bci_framework.paradigm.p300_paradigm.p300_basic.p300_basic_visual import P300Basic
from new_bci_framework.paradigm.p300_paradigm.p300_basic.p300_basic_audio import P300Basic_audio
from new_bci_framework.preprocessing.p300_preprocessing import P300Preprocessing
from new_bci_framework.recorder.opeb_bci_cyton_recorder import CytonRecorder
from new_bci_framework.recorder.test import main_test
from new_bci_framework.classifier.base_classifier import BaseClassifier
from new_bci_framework.config.config import Config
from new_bci_framework.paradigm.p300_paradigm.p300_paradigm import P300Paradigm
from new_bci_framework.preprocessing.preprocessing_pipeline import PreprocessingPipeline
from new_bci_framework.recorder.recorder import Recorder
from new_bci_framework.session.offline_session import OfflineSession
from new_bci_framework.session.session import Session

if __name__ == '__main__':
     root_dir = os.path.abspath(f'..{os.path.sep}sessions')
     subject_name = input("input subject name")
     kwargs = {'root_dir': root_dir, 'show_live_data': True}
     if subject_name:
         kwargs['subject_name'] = subject_name
     config = Config(**kwargs)

     session = OfflineSession(
        recorder=CytonRecorder(config, synthetic_data=True),
         paradigm=P300Basic_audio(config),
         preprocessor=P300Preprocessing(config),
         classifier=P300Classifier(config),
         config=config
     )
     session.run_all()
     main_test()

    #session: OfflineSession = OfflineSession.load_session("C:\Users\yarde\Documents\GitHub\BCI4ALS-MI\python\bci4als-2022-python\sessions\Session_2022-05-09_check-1")
