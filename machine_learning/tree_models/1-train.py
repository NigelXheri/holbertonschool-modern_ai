#!/usr/bin/env python3
"""Trains a tree-based classifier using Scikit-learn."""


def train_tree(clf, X, y):
    """Trains a tree-based classifier using Scikit-learn."""
    clf.fit(X, y)
