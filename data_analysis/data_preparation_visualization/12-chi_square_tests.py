#!/usr/bin/env python3
"""Test categorical features for independence from customer churn."""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Return each categorical feature's chi-square p-value against Churn."""
    categorical = df.select_dtypes(include=['object', 'string', 'category'])
    p_values = {}
    for feature in categorical.columns.drop('Churn', errors='ignore'):
        table = pd.crosstab(df[feature], df['Churn'])
        p_values[feature] = float(stats.chi2_contingency(table).pvalue)
    return p_values
