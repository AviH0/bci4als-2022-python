import random
import time

from ..paradigm.paradigm import Paradigm
from ..config.config import Config
from ..recorder.recorder import Recorder

NUM_TRIALS = 30

class DummyParadigm(Paradigm):
    """
    Dummy Paradigm subclass to use for testing.
    """

    def __init__(self, config: Config):
        super(DummyParadigm, self).__init__(config)
        # Set trial labels in config
        config.TRIAL_LABELS[5] = "Stim 1"
        config.TRIAL_LABELS[10] = "Stim 2"

    def start(self, recorder: Recorder):
        print(f"\n\n"
              f"=========================")
        print(f"starting dummy experiment")
        for i in range(1, NUM_TRIALS + 1):
            print(f"\t\tStarting Trial {i}")
            marker = random.choice([5, 10])
            trial_type = self._config.TRIAL_LABELS[marker]
            print(f"\t\tTrial is of type {trial_type} and marker is {marker}")
            recorder.push_marker(marker)
            print(f"\t\twaiting a little bit")
            time.sleep(1)
            print(f"\t\ttrial is over.")
            print(f"\t\t=========================\n\n")
        print(f"\n\n"
              f"=========================\n"
              "Experiment is over\n"
              "==========================")

