#!/usr/bin/env python3
"""Removes duplicates from dataframe"""


def remove_duplicates(df):
    """Removes duplicates from dataframe"""
    return df.drop_duplicates()
