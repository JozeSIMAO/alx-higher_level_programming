#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for integer in my_list:
        if isinstance(integer,int):
            print("{}".format(integer))
