#!/usr/bin/python3
"""defines a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation

    Args:
        my_obj: Object
        filename: file
    """
    with open(filename, "w") as file:
        json.dump(my_obj,file)
