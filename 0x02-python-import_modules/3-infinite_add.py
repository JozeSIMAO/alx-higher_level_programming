#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    num_args = len(sys.argv)
    sum = 0

    for counter in range(num_args - 1):
        sum += int(sys.argv[counter + 1])
    print("{}".format(total))
