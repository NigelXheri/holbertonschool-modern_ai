#!/usr/bin/env python3
"""Visualize categorical feature distributions."""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Show and save a grid of category counts for the selected columns."""
    if columns_to_plot is None:
        categorical = df.select_dtypes(include=['object', 'string'])
        columns = categorical.columns.drop('Churn', errors='ignore')
    else:
        columns = columns_to_plot

    n_cols = 3
    n_rows = max(1, (len(columns) + n_cols - 1) // n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.ravel()

    for ax, column in zip(axes, columns):
        counts = df[column].value_counts()
        ax.bar(counts.index.astype(str), counts)
        ax.set_title(column)
        ax.tick_params(axis='x', labelrotation=45)

    for ax in axes[len(columns):]:
        fig.delaxes(ax)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
