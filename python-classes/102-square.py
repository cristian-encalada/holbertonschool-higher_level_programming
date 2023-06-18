#!/usr/bin/python3
""" Task 9. Compare 2 squares
"""


class Square:
    """Defines a square
    """
    def __init__(self, size=0):
        """Initialize the Square object with a given size (default = 0)
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate the area of the square
        """
        return self.__size**2

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()
