#!/usr/bin/python3
"""Defines a class Base"""
import json


class Base:
    """Represents the Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base

        Args:
            id (int): Id of new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))
