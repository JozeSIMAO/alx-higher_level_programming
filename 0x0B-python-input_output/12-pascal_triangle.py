#!/usr/bin/python3
"""defines a function that prints pascals triangle"""


def pascal_triangle(n):
    """represents a pascal triangle of size n

    returns: a list of lists of integers representing
        pascals triangle of (n)
    """
    if n <= 0:
        return ([])

    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_number = previous_row[j - 1] + previous_row[j]
            new_row.append(new_number)

        new_row.append(1)
        triangle.append(new_row)

    return (triangle)
