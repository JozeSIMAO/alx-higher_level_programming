#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """a function that deletes the item at a specific position"""
    new_list = []

    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
