#!/usr/bin/python3
# 0-add_integer.py
"""defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
        a: 1st integer
        b: 2nd integer

    Raises:
        TypeError: If either of a or b is a non-integer and not a flot
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
