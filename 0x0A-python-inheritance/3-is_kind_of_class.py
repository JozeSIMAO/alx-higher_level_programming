#!/usr/bin/python3
"""Defines a function that returns true of false"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class/otherwise False


    Args:
        obj: object
        a_class: class
    """
    return (isinstance(obj, a_class))
