#!/usr/bin/env python3
"""Remove the customer identifier from a DataFrame."""


def drop_customerID(df):
    """Return the DataFrame with the customerID column removed."""
    return df.drop(columns=['customerID'])
