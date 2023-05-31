#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz".format(num), end=' ')
        elif (num % 3 == 0):
            print("Fizz".format(num), end=' ')
        elif (num % 5 == 0):
            print("Buzz".format(num), end=' ')
        else:
            print("{}".format(num), end=' ')
