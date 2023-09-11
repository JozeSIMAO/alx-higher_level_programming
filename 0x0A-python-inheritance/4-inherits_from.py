#!/usr/bin/python3
"""defines a function that returns true or false"""


def inherits_from(obj, a_class):
    """returns true or false if the object is an instance of that inheretied
    directed or indirectly from the specified class

    Args:
        obj: object
        a_class: class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
