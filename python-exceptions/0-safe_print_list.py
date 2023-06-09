#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for item in my_list:
            if length < x:
                print(item, end='')
                length += 1
    except ValueError():
        print("Index out of range")
    finally:
        print()
        return length
