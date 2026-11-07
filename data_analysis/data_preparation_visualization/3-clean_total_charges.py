#!/usr/bin/env python3
"""Handle missing values in TotalCharges."""


def clean_total_charges(df, method='drop'):
    """Handle missing values in TotalCharges."""

    if method in ('median', 'impute'):
        df = df.copy()

    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])

    elif method == 'median':
        median = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median)

    elif method == 'impute':
        values = df['MonthlyCharges'] * df['tenure']
        df['TotalCharges'] = df['TotalCharges'].fillna(values)

    return df
