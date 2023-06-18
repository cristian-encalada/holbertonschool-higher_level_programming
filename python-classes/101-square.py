#!/usr/bin/python3
""" Task 8. Print Square instance
"""


class Square:
    """Define a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the data
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the value of position
        """
        is_tuple = isinstance(value, tuple)
        is_valid_length = len(value) == 2
        is_positive_int = all(
            isinstance(val, int) and val >= 0 for val in value)

        if not (is_tuple and is_valid_length and is_positive_int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square
        """
        return self.__size**2

    def my_print(self):
        """Print in stdout a square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Same behavior as my_print()
        """
        sq_str = ""
        if self.__size == 0:
            sq_str += "\n"
        else:
            for _ in range(self.__position[1]):
                sq_str += "\n"

            for _ in range(self.__size):
                sq_str += " " * self.__position[0] + "#" * self.__size + "\n"

        return sq_str.rstrip()
