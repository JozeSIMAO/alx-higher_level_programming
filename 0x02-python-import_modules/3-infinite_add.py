#!/usr/bin/python3
import sys
# A program that prints the result of the addition of all arguments
# Followed by a new line

counter = 1
num_args = len(sys.argv)
sum = 0

while counter < num_args:
    sum = sum + int(sys.argv[counter])
    counter += 1
print(f"{sum}")
