from collections import OrderedDict
from typing import Dict, Tuple

import mne
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from mne.decoding import Vectorizer
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_val_score, StratifiedShuffleSplit, train_test_split
from pyriemann.estimation import ERPCovariances, XdawnCovariances, Xdawn
from pyriemann.tangentspace import TangentSpace
from pyriemann.classification import MDM

from new_bci_framework.classifier.base_classifier import BaseClassifier
from new_bci_framework.config.config import Config


class P300Classifier(BaseClassifier):

    def __init__(self, config: Config):
        super().__init__(config)
        self.clfs = OrderedDict()
        self.clfs['Vect + LR'] = make_pipeline(Vectorizer(), StandardScaler(), LogisticRegression())
        self.clfs['Vect + RegLDA'] = make_pipeline(Vectorizer(), LDA(shrinkage='auto', solver='eigen'))
        self.clfs['Xdawn + RegLDA'] = make_pipeline(Xdawn(2, classes=[1]), Vectorizer(),
                                                    LDA(shrinkage='auto', solver='eigen'))

        self.clfs['XdawnCov + TS'] = make_pipeline(XdawnCovariances(estimator='oas'), TangentSpace(),
                                                   LogisticRegression())
        self.clfs['XdawnCov + MDM'] = make_pipeline(XdawnCovariances(estimator='oas'), MDM())

        self.clfs['ERPCov + TS'] = make_pipeline(ERPCovariances(), TangentSpace(), LogisticRegression())
        self.clfs['ERPCov + MDM'] = make_pipeline(ERPCovariances(), MDM())
        self.event_dict: Dict[str, int] = dict()

    def run(self, data: mne.Epochs):
        data.load_data()
        self.event_dict = {v: k for k, v in self._config.TRIAL_LABELS.items()}
        train, test = self.train_test_split(data, test_size=0.3)
        self.fit(train)
        self.evaluate(test)

    def fit(self, data: mne.Epochs):

        X = data.get_data() * 1e6
        times = data.times
        y = data.events[:, -1]

        cv = StratifiedShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
        labels = y == self.event_dict['Target']
        num_target = np.sum(y)
        num_non_target = len(y) - num_target
        weights = y * (num_non_target / len(y)) + (~y) * (num_target / len(y))
        auc = []
        methods = []
        for m in self.clfs:
            try:
                self.clfs[m].fit(X, y)
            except ValueError as e:
                print(e)
            # res = cross_val_score(self.clfs[m], X, y == event_dict['Target'], scoring='balanced_accuracy', cv=1, n_jobs=-1)
            # auc.extend(res)
            # methods.extend([m] * len(res))

        # results = pd.DataFrame(data=auc, columns=['Accuracy'])
        # results['Method'] = methods
        #
        # plt.figure(figsize=[8, 4])
        # sns.barplot(data=results, x='Accuracy', y='Method')
        # plt.xlim(0.0, 1.0)
        # sns.despine()

    def predict(self, data: mne.Epochs):
        pass

    def evaluate(self, data: mne.Epochs):
        X = data.get_data() * 1e6
        times = data.times
        y = data.events[:, -1]

        cv = StratifiedShuffleSplit(n_splits=1, test_size=0.25, random_state=42)

        auc = []
        methods = []

        labels = y == self.event_dict['Target']
        num_target = np.sum(labels)
        num_non_target = len(y) - num_target
        weights = y * (num_non_target/len(y)) + (~y) * (num_target/len(y))
        for i, m in enumerate(self.clfs):
            try:
                res = self.clfs[m].score(X, y, weights)
                fig, ax = plt.subplots()
                ax.set_title(m)
                classes = list(self._config.TRIAL_LABELS.keys())
                labels = [self._config.TRIAL_LABELS[val] for val in classes]
                conf = ConfusionMatrixDisplay.from_estimator(self.clfs[m], X, y, ax=ax, labels=classes, display_labels=labels)
                conf.plot(ax=ax)
                fig.show()
            except:
                res = 0
            # res = cross_val_score(self.clfs[m], X, y == event_dict['Target'], scoring='balanced_accuracy', cv=1, n_jobs=-1)
            # auc.extend(res)
            auc.append(res)
            # methods.extend([m] * len(res))
            methods.append(m)

        results = pd.DataFrame(data=auc, columns=['Accuracy'])
        results['Method'] = methods
        #
        plt.figure(figsize=[8, 4])
        sns.barplot(data=results, y='Accuracy', x='Method')
        plt.xlim(0.0, 1.0)
        sns.despine()

    def train_test_split(self, data: mne.Epochs, test_size=0.25) -> Tuple[mne.Epochs, mne.Epochs]:
        train_indxs, test_indxs = train_test_split(np.arange(len(data)), test_size=test_size,
                                                   random_state=654321)
        return data[train_indxs], data[test_indxs]
