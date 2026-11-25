#!/usr/bin/env python3
"""Displays the textual structure of a trained decision tree classifier."""
from sklearn import tree


def draw(clf, feature_names, class_names):
    """Displays the textual structure of a trained decision tree classifier."""
    tree_rules = tree.export_text(clf,
                                  feature_names=feature_names,
                                  class_names=class_names)
    print(tree_rules)
