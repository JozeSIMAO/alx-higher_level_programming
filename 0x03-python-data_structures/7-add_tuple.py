#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """a function that adds 22 tuples"""
    p_tuple_a = tuple_a + (0, 0)
    p_tuple_b = tuple_b + (0, 0)

    new_tuple = (p_tuple_a[0] + p_tuple_b[0], p_tuple_a[1] + p_tuple_b[1])
    return new_tuple
