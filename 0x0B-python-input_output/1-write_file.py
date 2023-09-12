#!/usr/bin/python3
"""defines a function that writes to a file"""


def write_file(filename="", text=""):
    """writes to a file (utf-8) and returns the number of characters

    Args:
        filename: file to write to
        text: text to write
    returns: num of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        num_chars = file.write(text)
    return (num_chars)
