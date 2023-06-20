#!/usr/bin/python3
""" Task 7. Integer validator
"""


class BaseGeometry:
    """BaseGeometry class
    """
    def area(self):
        """Raise an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value
        """
        self.name = name
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
