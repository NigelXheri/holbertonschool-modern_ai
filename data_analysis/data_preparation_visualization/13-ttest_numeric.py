#!/usr/bin/env python3
"""Compare numeric features across churn groups with Welch's t-test."""
from scipy import stats


def ttest_numeric(df):
    """Return two-sided Welch t-test p-values for numeric features."""
    features = df.select_dtypes(include='number').columns
    yes = df.loc[df['Churn'] == 'Yes', features]
    no = df.loc[df['Churn'] == 'No', features]

    p_values = {}
    for feature in features:
        test = stats.ttest_ind(yes[feature].dropna(), no[feature].dropna(),
                               equal_var=False)
        p_values[feature] = float(test.pvalue)
    return p_values
