#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    counter = 1
    num_args = len(sys.argv)
    sum = 0

    while counter < num_args:
        sum = sum + int(sys.argv[counter])
        counter += 1
    print("{}".format(total))
