#!/usr/bin/env python3
"""Standardize the charge features."""
from sklearn import preprocessing


def scale_numeric(df):
    """Return a copy with MonthlyCharges and TotalCharges standardized."""
    columns = ['MonthlyCharges', 'TotalCharges']
    scaled = df.copy()
    scaler = preprocessing.StandardScaler()
    scaled[columns] = scaler.fit_transform(df[columns])
    return scaled
