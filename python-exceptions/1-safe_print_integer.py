#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if type(value) == int:
            print("{:d}".format(value))
            return True
    except (ValueError(), TypeError()):
        print("Not an integer")
        return False
