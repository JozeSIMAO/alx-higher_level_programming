#!/usr/bin/python3
"""Defines a class BaseGeomeytry"""


class BaseGeometry:
    """represents a class BaseGeometry"""

    def area(self):
        """not impimented instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): name
            value (int): value
        Raises:
            TypeError: if value is not of (int)
            VAlueErro: value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
