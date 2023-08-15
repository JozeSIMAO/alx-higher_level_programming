#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """a function that deletes the item at a specific position"""
    new_list = []

    if idx < 0 or idx >= len(my_list):
        return my_list

    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return new_list
