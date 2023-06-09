#!/usr/bin/python3
def safe_print_integer(value):
    length = 0
    try:
        if type(value) == int:
            print("{:d}".format(value))
            return True
    except ValueError():
        return False
