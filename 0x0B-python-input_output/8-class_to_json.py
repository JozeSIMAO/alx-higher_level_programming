#!/usr/bin/python3
"""defines a function (class_to_JSON)"""


def class_to_json(obj):
    """returns the dictionary description"""
    return (obj.__dict__)
