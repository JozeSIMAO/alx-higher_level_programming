#!/usr/bin/python3
"""defines a function that returns the JSON repre of an object/str"""
import json


def to_json_string(my_obj):
    """returns JSON representation of an object (str)

    Args:
        my_obj: object (string)
    returns: object representation of string
    """
    return (json.dumps(my_obj))
