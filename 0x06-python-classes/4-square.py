#!/usr/bin/python3
"""defines a class square"""


class Square:
    """"represents a square

    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initializes a square instance

        Args:
            size (int, optional): Size of the square. defaults to 0
        """
        self.__size = size

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute
        Args: value (int): Size value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be a integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area of a square and returns it"""
        return self.__size ** 2
