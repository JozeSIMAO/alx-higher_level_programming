#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """a function that computes the square value of int in a matrix"""
    squared_matrix = matrix.copy()

    for i in range(len(matrix)):
        squared_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return squared_matrix
