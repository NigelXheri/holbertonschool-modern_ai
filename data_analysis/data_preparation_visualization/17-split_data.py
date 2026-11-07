#!/usr/bin/env python3
"""Split a dataset into stratified training and test sets."""
from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """Return training and test features and labels, stratified by target."""
    features = df.drop(columns=[target])
    labels = df[target]
    return model_selection.train_test_split(
        features, labels, test_size=test_size, random_state=random_state,
        stratify=labels
    )
