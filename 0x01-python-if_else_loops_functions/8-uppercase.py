#!/usr/bin/python3

def uppercase(str):
    # Prints a string in uppercase followed by a new line

    for char in str:
        if ord(char) >= 97 <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
