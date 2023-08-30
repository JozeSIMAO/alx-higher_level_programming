#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a square


    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size):
        """Initializes a square instance

        Args:
            size (int, optional): Size of the square, defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Getter Method for the size attribut"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter methodfor the size attribute

        Args:
            value (int): Size value to set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square and returns it"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with "#" character to stdout"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
