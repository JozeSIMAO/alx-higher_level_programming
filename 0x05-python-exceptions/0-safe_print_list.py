#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list"""
    counter = 0

    for elem in range(x):
        try:
            print("{}".format(my_list[elem]), end='')
            counter += 1
        except IndexError:
            break
    print("")
    return counter
