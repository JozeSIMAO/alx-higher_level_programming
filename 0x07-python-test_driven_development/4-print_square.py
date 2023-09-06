#!/usr/bin/python3
"""defines a function that prints a square with the character '#'"""


def print_square(size):
    """prints a square with the character '#'

        Args:
            size: is the length of the square

        raises:
            ValueError: exception
            TypeError: exception

        returns: the square in '#' format
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
