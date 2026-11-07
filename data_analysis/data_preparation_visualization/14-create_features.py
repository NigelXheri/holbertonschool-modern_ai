#!/usr/bin/env python3
"""Engineer service-count and tenure-group features."""
import pandas as pd


def create_features(df):
    """Return a DataFrame with service counts and tenure bands."""
    services = [
        'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies',
    ]
    internet = df['InternetService'].isin(['DSL', 'Fiber optic'])
    counts = df[services].eq('Yes').sum(axis=1) + internet
    groups = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, float('inf')],
        labels=['0-12', '13-24', '25-48', '49-60', '60+'],
    )
    result = df.drop(columns=services + ['InternetService', 'tenure'])
    return result.assign(NumServices=counts, TenureGroup=groups)
