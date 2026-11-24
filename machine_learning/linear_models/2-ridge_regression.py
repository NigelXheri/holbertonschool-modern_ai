#!/usr/bin/env python3
"""Creates and returns a Ridge Regression model using Scikit-learn"""
from sklearn import linear_model


def ridge_regression(random_state):
    """Creates and returns a Ridge Regression model using Scikit-learn"""
    return linear_model.Ridge(random_state=random_state)
