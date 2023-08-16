#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list, just once for each int"""
    new_list = set(my_list)
    sum = 0

    for num in new_list:
        sum += num

    return sum
