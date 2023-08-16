#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""

    ordered_dict = sorted(a_dictionary.keys())

    for key in ordered_dict:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
