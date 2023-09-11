#!/usr/bin/python3
"""define a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a class Square"""

    def __init__(self, size):
        """creates a new square

        Args:
            size (int): is size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
