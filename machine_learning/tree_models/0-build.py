#!/usr/bin/env python3
"""Creates a decision tree classifier using Scikit-learn."""
from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """Creates a decision tree classifier using Scikit-learn."""
    return tree.DecisionTreeClassifier(criterion='gini',
                                       min_samples_leaf=min_samples_leaf,
                                       min_samples_split=min_samples_split,
                                       random_state=random_state)
