#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list"""
    try:
        counter = 0

        for elem in range(x):
            print(my_list[elem], end=' ')
            counter += 1
    except IndexError:
            pass

    print()
    return counter
