#!/usr/bin/python3
"""defines a function that returns an object represented by a JSON str"""
import json


def from_json_string(my_str):
    """returns the python object representation of a JSON string

    Args:
        my_str: JSON String
    return: object representation of the JSON string
    """
    return (json.loads(my_str))
