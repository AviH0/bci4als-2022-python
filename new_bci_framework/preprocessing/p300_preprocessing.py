from typing import List, Dict

import mne
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from new_bci_framework.config.config import Config
from new_bci_framework.preprocessing.preprocessing_pipeline import PreprocessingPipeline


class P300Preprocessing(PreprocessingPipeline):

    def __init__(self, config: Config):
        super().__init__(config)

    def run_pipeline(self, data: mne.io.Raw) -> mne.Epochs:
        epochs = super().run_pipeline(data)
        event_dict: Dict[str, int] = {v: k for k, v in self._config.TRIAL_LABELS.items()}
        evks = dict()
        figs: List[Figure] = []
        for label in event_dict:
            erps = epochs[label].average()
            evks[label] = erps
            fig_title = f"average evoked response for {label}"
            fig = mne.evoked.plot_evoked(erps, show=False, spatial_colors=True, window_title=fig_title)
            fig.suptitle(fig_title)
            figs.append(fig)
        figs += mne.viz.plot_compare_evokeds(evks, show=False, picks='eeg', axes='topo')

        for i, fig in enumerate(figs):
            fig.set_size_inches(20, 10)
            fig.savefig(
                f"{self._save_dir}/{fig.texts[0].get_text() if fig.texts and fig.texts[0] else 'figure_' + str(i)}.png")
        if self._config.SHOW_PLOTS:
            plt.show(block=False)
        return epochs
