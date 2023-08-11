#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    num_args = len(sys.argv)
    sum = 0
    counter = 0

    while counter < (num_args - 1):
        sum = sum + int(sys.argv[counter + 1])
    print("{}".format(total))
