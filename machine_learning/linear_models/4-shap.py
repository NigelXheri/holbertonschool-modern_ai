#!/usr/bin/env python3
"""Helps generate model explanations using the SHAP library"""
import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Helps generate model explanations using the SHAP library"""
    return (shap.Explainer(model), shap.Explainer(model)(X_train, X_test))
