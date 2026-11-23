#!/usr/bin/env python3
"""Computes common evaluation metrics for regression tasks."""
from sklearn import metrics
import numpy as np


def evaluation_metrics_for_regression(y_true, y_pred):
    """Computes common evaluation metrics for regression tasks."""
    return (metrics.mean_squared_error(y_true, y_pred),
            metrics.root_mean_squared_error(y_true, y_pred),
            metrics.mean_absolute_error(y_true, y_pred),
            metrics.r2_score(y_true, y_pred))
