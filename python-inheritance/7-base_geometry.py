#!/usr/bin/python3
""" Task 7. Integer validator
"""


class BaseGeometry:
    """ Class BaseGeometry based on 6-base_geometry.py
    """
    def area(self):
        """ Not implemented yet
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate value, assume <name> is always a string
        """
        if not isinstance(value, int):
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
