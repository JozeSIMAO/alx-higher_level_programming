#!/usr/bin/python3
"""defines a function that creates an object from a JSON File"""
import json


def load_from_json_file(filename):
    """creates an objecct from JSON file

    Args:
        filename: file
    """
    with open(filename) as file:
        return (json.load(file))
