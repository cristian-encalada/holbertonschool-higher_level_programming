#!/usr/bin/python3
""" Task 1. My list
"""


class MyList(list):
    """ Print a list sorted in ascending order
    """
    def print_sorted(self):
        print(sorted(self))
