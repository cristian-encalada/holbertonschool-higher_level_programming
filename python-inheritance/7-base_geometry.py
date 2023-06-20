#!/usr/bin/python3
""" Task 7. Integer validator
"""


class BaseGeometry:
    """ Class BaseGeometry based on 6-base_geometry.py
    """

    def area(self):
        """ Not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate value, assume <name> is always a string
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
