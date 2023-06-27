#!/usr/bin/python3
"""Task 2. First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Clas Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # getters
    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    # setters
    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        self.__y = value
