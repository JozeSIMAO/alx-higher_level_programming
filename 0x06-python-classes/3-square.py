#!/usr/bin/python3
"""define a class square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """initializes a new square
        Args:
            size (int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of the square and returns it"""
        return self.__size ** 2
