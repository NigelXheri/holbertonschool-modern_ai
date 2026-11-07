#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Display one vertical marker for every missing DataFrame value."""
    plt.figure(figsize=(12, 8))
    rows, columns = np.where(df.isna().to_numpy())
    plt.scatter(df.index[rows], columns, marker='|')
    plt.yticks(range(len(df.columns)), df.columns)
    plt.tight_layout()
    plt.show()
