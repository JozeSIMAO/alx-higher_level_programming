#!/usr/bin/python3
def add_integer(a, b=98):
    """a function that adds 2 integer"""
    answer = 0

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    answer = a + b
    return (answer)
