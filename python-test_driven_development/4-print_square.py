#!/usr/bin/python3
"""
Task 3. Print a square
"""


def print_square(size):
    """
    Print in stdout a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and size < 0:
        raise ValueError("size must be an integer")

    for _ in range(size):
        print('#' * size)
