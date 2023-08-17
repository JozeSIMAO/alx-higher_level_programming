#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """returns a list with values multiplied bya number"""
    new_list = list(map(lambda x: x * number, my_list))

    return new_list
