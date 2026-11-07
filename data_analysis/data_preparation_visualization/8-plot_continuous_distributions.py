#!/usr/bin/env python3
"""Visualize distributions of continuous numerical features."""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Display and save histograms with KDE curves and horizontal boxplots."""
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(include='number').columns

    n_rows = max(1, len(columns_to_plot))
    fig, axes = plt.subplots(n_rows, 2, figsize=(10, 3 * n_rows),
                             squeeze=False)

    for column, (histogram, boxplot) in zip(columns_to_plot, axes):
        values = df[column].dropna().to_numpy(dtype=float)
        values = values[np.isfinite(values)]
        if values.size:
            histogram.hist(values, bins=30, density=True, alpha=0.7,
                           edgecolor='black')
            if values.min() < values.max():
                kde = stats.gaussian_kde(values)
                points = np.linspace(values.min(), values.max(), 200)
                histogram.plot(points, kde(points), color='red',
                               linestyle='--')

        histogram.set_title(f'{column} Histogram + KDE')
        boxplot.boxplot(values, vert=False)
        boxplot.set_title(f'{column} Boxplot')

    if len(columns_to_plot) == 0:
        for ax in axes.flat:
            fig.delaxes(ax)

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
