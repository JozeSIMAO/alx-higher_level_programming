#!/usr/bin/python3
"""defines a class MyList that inherits from list"""


class MyList(list):
    """inherits from list


    Args:
        list: class
    """
    def print_sorted(self):
        """prints the list, in ascending order"""
        print(sorted(self))
