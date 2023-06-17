#!/usr/bin/python3
"""Task 4. Eval is magic
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object data
        """
        self.width = width
        self.height = height

    """Getter methods to retreve the value
    """

    @property
    def width(self):
        """Getter method of width
        """
        return self.__width

    @property
    def height(self):
        """Getter method of height
        """
        return self.__height

    """Setter methods to set the value
    """

    @width.setter
    def width(self, value):
        """Setter method of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter method of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """Rectangle methods
    """

    def area(self):
        """Calculate the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Print a rectangle with the character #
        """
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    s += '#'
                if i != self.__height - 1:
                    s += '\n'
        return s

    def __repr__(self):
        "Return a string representation of the rectangle"
        return f'Rectangle({self.__width}, {self.__height})'
