#!/usr/bin/python3
""" Task 31. Low memory cost
"""


class LockedClass:
    """ Prevent the user from dynamically creating new instance attributes,
    except if the new instance attribute is called 'first_name'
    """
    __slots__ = ["first_name"]
