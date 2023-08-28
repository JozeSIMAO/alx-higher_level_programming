#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers"""
    counter = 0
    try:
        for values in range(x):
            if isinstance(my_list[values], int):
                print("{:d}".format(my_list[values]))
                counter += 1
    except (IndexError, TypeError):
        pass

    return counter
