#!/usr/bin/env python3
"""Compare numeric feature distributions by churn status."""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Display the two churn groups in a histogram with shared bin edges."""
    labels = ['No', 'Yes']
    groups = [df.loc[df['Churn'] == label, col].dropna() for label in labels]

    plt.figure(figsize=(12, 8))
    plt.hist(groups, bins=30, label=labels)
    plt.title(f'{col} Distribution by Churn')
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()
