#!/usr/bin/env python3
"""Visualize the distribution of customer churn."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Display counts for customers who stayed and customers who churned."""
    counts = df['Churn'].value_counts().reindex(['No', 'Yes'], fill_value=0)

    plt.figure(figsize=(12, 8))
    plt.bar(counts.index, counts, color=['skyblue', 'salmon'])
    plt.title('Churn Distribution')
    plt.ylabel('Count')
    plt.show()
