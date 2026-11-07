#!/usr/bin/env python3
"""Encode customer features for modeling."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Return encoded data and fitted churn, binary, and tenure encoders."""
    encoded = df.copy()
    binary_columns = ['Partner', 'Dependents', 'PaperlessBilling',
                      'SeniorCitizen']
    tenure_column = ['TenureGroup']

    churn_encoder = preprocessing.LabelEncoder().fit(['No', 'Yes'])
    binary_encoder = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])
    binary_encoder.fit([['No'], ['Yes']])
    tenure_encoder = preprocessing.OrdinalEncoder()

    encoded['Churn'] = churn_encoder.transform(df['Churn']).astype('int64')
    for column in binary_columns:
        values = df[[column]].to_numpy()
        encoded[column] = binary_encoder.transform(values).ravel().astype(
            'int64'
        )
    tenure_values = tenure_encoder.fit_transform(df[tenure_column])
    encoded[tenure_column] = tenure_values.astype('int64')
    encoded = pd.get_dummies(encoded, columns=['Contract', 'PaymentMethod'],
                             drop_first=True, dtype='int64')
    return encoded, churn_encoder, binary_encoder, tenure_encoder
