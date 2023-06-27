#!/usr/bin/python3
"""Task 2. First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Clas Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
