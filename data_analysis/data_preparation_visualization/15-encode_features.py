#!/usr/bin/env python3
"""Encode customer features for modeling."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Return encoded data and the fitted churn, binary, and tenure encoders."""
    encoded = df.copy()
    binary_columns = ['Partner', 'Dependents', 'PaperlessBilling',
                      'SeniorCitizen']
    tenure_column = ['TenureGroup']

    churn_encoder = preprocessing.LabelEncoder().fit(['No', 'Yes'])
    binary_encoder = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']] * len(binary_columns), dtype='int64'
    )
    tenure_encoder = preprocessing.OrdinalEncoder(dtype='int64')

    encoded['Churn'] = churn_encoder.transform(df['Churn']).astype('int64')
    encoded[binary_columns] = binary_encoder.fit_transform(df[binary_columns])
    encoded[tenure_column] = tenure_encoder.fit_transform(df[tenure_column])
    encoded = pd.get_dummies(encoded, columns=['Contract', 'PaymentMethod'],
                             drop_first=True, dtype='int64')
    return encoded, churn_encoder, binary_encoder, tenure_encoder
