#!/usr/bin/python3
"""defines a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_b should contain only integers or floats")

    m_a_cols = len(m_a[0])
    m_b_cols = len(m_b[0])
    if not all(len(row) == m_a_cols for row in m_a):
        raise("Each row of m_a must be of the same size")
    if not all(len(row) == m_b_cols for row in m_b):
        raise TypeError("Each row of m_b must be of the same size")

    if m_a_cols != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(m_b_cols)] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(m_b_cols):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return (result)
