#!/usr/bin/python3
"""defines a function that returns the list of avail attributes and methods"""


def lookup(obj):
    """A function that returns a list object

    Args:
        obj: object to search in
    """
    attri_methods = dir(obj)

    return attri_methods
