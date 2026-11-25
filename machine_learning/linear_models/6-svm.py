#!/usr/bin/env python3
"""Creates an SVM Classifier."""
from sklearn import svm


def get_SVM_model(name, random_state):
    """Creates an SVM Classifier."""
    if name not in ['linear', 'poly', 'rbf']:
        return None
    return svm.SVC(kernel=name, random_state=random_state)
