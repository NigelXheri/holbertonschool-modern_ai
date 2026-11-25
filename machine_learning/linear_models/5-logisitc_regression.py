#!/usr/bin/env python3
"""Creates a logistic Regression model."""
from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Creates a logistic Regression model."""
    return linear_model.LogisticRegression(random_state=random_state)
