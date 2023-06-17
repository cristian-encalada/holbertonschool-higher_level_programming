#!/usr/bin/python3
"""Task 1. Real definition of a rectangle
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object data"""
        self.__width = width
        self.__height = height

    """Getter methods to retreve the value"""

    @property
    def width(self):
        """Getter method of width"""
        return self.__width

    @property
    def height(self):
        """Getter method of height"""
        return self.__height

    """Setter methods to set the value"""

    @width.setter
    def width(self, value):
        """Setter method of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter method of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
