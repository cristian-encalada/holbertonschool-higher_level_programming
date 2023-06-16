#!/usr/bin/python3
""" Task 5. Printing a square
"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """Initialize the Square object with a given size (default = 0)"""
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the area of the square"""
        return self.__size**2

    def my_print(self):
        """Print in stdout a square with the character #"""
        if self.__size == 0:
            print()

        for _ in range(self.__size):
            print("#" * self.__size)
