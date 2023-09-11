#!/usr/bin/python3
"""defines a function that returs True if theobject is
excalty an instance of the specified class"""


def is_same_class(obj, a_class):
    """checks if the obj and the class are an exact instance

    Arg:
        obj: object
        a_class: class
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
