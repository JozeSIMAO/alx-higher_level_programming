#!/usr/bin/python3
def fizzbuzz():

    # prints the numbers from 1 to 100 separated by a space

    for number in range(1 , 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{} ".format(number),end="")