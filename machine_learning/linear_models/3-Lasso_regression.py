#!/usr/bin/env python3
"""Creates and returns a Lasso Regression model using Scikit-learn"""
from sklearn import linear_model


def lasso_regression(random_state):
    """Creates and returns a Lasso Regression model using Scikit-learn"""
    return linear_model.Lasso(random_state=random_state)
