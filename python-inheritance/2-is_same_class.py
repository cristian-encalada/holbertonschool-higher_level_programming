#!/usr/bin/python3
""" Task 2. Exact same object
"""


def is_same_class(obj, a_class):
    """ Return True if the object is exactly an instance of the specified class
    """
    return True if type(obj) is a_class else False
