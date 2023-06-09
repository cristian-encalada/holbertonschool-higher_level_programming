#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except (ValueError(), TypeError()):
        print("Error: The value is not an integer")
        return False
