#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    # A program that imports functions from the calculator_1.py file
    # and does some Maths and then prints the results

    a = 10
    b = 5

    print("{} + {} =".format(add(a, b)))
    print("{} - {} =".format(sub(a, b)))
    print("{} * {} =".format(mul(a, b)))
    print("{} / {} =".format(div(a, b)))
