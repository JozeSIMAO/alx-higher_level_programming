#!/usr/bin/python3
"""defines a function that reads a text file"""


def read_file(filename=""):
    """reads a text and prints it to stdout

    Args:
        filename: file to read and print
    """
    with open(filenam, encoding="utf-8"e) as file:
        print(file.read(), end="")
