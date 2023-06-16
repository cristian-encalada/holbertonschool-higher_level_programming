#!/usr/bin/python3
""" Task 3. Area of a square
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialize the Square object with a given size (default = 0)"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the area of the square"""
        return self.__size**2
