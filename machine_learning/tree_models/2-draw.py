#!/usr/bin/env python3
"""Displays the textual structure of a trained decision tree classifier."""


def draw(clf, feature_names, class_names):
    """Displays the textual structure of a trained decision tree classifier."""
    clf.export_text(feature_names=feature_names, class_names=class_names)
