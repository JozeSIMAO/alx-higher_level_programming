#!/usr/bin/python3
import sys
# A program that prints the number of
# and the lists of its arguments

num_args = len(sys.argv)
counter = 1

if num_args == 1:
    print("0 arguments.")
elif num_args > 1:
    print(f"{num_args - 1} arguments:")
    while counter < num_args:
        print(f"{counter}: {sys.argv[counter]}")
        counter += 1
