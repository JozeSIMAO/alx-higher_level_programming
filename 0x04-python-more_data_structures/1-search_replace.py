#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another ina new list"""
    new_list = my_list.copy()

    for i in range(len(my_list)):
        if search == my_list[i]:
            new_list[i] = replace

    return new_list