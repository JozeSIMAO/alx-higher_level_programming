#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """a function that returns a set of all elem in only 1 set"""
    diff_set = set_1 ^ set_2
    return diff_set
