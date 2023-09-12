#!/usr/bin/python3
"""defines a function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a file (utf-8)

    Args:
        filename: file to append to
        text: text to append
    returns: num of chars added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        added_chars = file.write(text)
    return (added_chars)
