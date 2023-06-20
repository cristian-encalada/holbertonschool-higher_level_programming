#!/usr/bin/python3
""" Task 9. Full Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """ Instantiation
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate the area of a Rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """ Print a Rectangle with this format: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__height}/{self.__width}"
