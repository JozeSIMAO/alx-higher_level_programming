#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """a function that prints a matrix of integers"""
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end=' ' if i != row[-1] else '')
        print()
