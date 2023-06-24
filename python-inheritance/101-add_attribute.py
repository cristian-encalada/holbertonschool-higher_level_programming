#!/usr/bin/python3
"""Task 13. Can I?
"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if it's possible
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
