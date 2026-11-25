#!/usr/bin/env python3
"""Generates predictions from a trained tree-based classifier."""


def generate_predictions(clf, X):
    """Generates predictions from a trained tree-based classifier."""
    return clf.predict(X)
