#!/usr/bin/env python3
"""Generates a detailed classification report."""
from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """Generates a detailed classification report."""
    return metrics.classification_report(true_labels,
                                         predicted_labels,
                                         target_names=class_names)
