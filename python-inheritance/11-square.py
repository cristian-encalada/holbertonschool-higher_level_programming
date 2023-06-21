#!/usr/bin/python3
""" Task 11. Square # 2
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """ Instantiation
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Print a Square with this format: [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"