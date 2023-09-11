#!/usr/bin/python3
"""defines a function that returns the list of avail attributes and methods"""


def lookup(obj):
    """A function that returns a list object

    Args:
        obj: object to search in
    """
    attri_methods = dir(obj)

    methods = [item for item in attri_methods if callable(getattr(obj, item))]

    return methods
