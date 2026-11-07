#!/usr/bin/env python3
"""Visualize correlations between numeric features."""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Display an annotated Pearson correlation matrix."""
    correlations = df.select_dtypes(include='number').corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(correlations, annot=True, fmt='.2g', cmap='coolwarm',
                vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    plt.show()
