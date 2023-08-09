#!/usr/bin/python3
def print_last_digit(number):
    # prints the last digit of a number
    # returns the value of the last digit

    print(abs(number) % 10, end='')
    return (abs(number) % 10)
    # The last digit of a number is the remainder when
    # the number is divided by 10.
