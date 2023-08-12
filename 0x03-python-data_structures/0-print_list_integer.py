#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """a function that prints all integers of a list"""
    for integer in range(len(my_list)):
        print("{}".format(my_list[integer]))
