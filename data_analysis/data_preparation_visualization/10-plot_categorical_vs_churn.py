#!/usr/bin/env python3
"""Visualize churn rates by category."""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Display the proportion of customers who churned in each category."""
    churned = df['Churn'].eq('Yes')
    rates = churned.groupby(df[col], sort=True, observed=True).mean()

    plt.figure(figsize=(12, 8))
    plt.bar(rates.index.astype(str), rates)
    plt.title(f'Churn Rate by {col}')
    plt.ylabel('Churn Rate')
    plt.xticks(rotation=45)
    plt.show()
