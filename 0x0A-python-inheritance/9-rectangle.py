#!/usr/bin/python3
"""defines a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from base geometry"""

    def __init__(self, width, height):
        """creates a new Rectangle

        Args:
            width (int): width
            height (int): height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the print and str representation of the rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def __repr__(self):
        """returns the same string as __str__"""
        return (self.__str__())
