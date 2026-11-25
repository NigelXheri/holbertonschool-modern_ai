#!/usr/bin/env python3
"""Explain regression predictions with SHAP."""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Returns SHAP explainer object and values."""
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
