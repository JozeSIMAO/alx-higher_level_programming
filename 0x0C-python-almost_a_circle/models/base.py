#!/usr/bin/python3
"""Defines a class Base"""


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
