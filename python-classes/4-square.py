#!/usr/bin/python3
''' Task 4. Access and update private attribute

    Requirements:
    ------------
    - Write a class Square that defines a square by: (based on 3-square.py)

    - Private instance attribute: size:
        - property def size(self): to retrieve it
        - property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a TypeError exception
                with the message size must be an integer
            - if size is less than 0, raise a ValueError exception
                with the message size must be >= 0
    - Instantiation with optional size: def __init__(self, size=0):
    - Public instance method: def area(self): returns the current square area
    - Is not allowed to import any module
'''


class Square:
    '''Defines a square'''
    def __init__(self, size=0):
        '''Initialize the Square object with a given size (default = 0)'''
        self.__size = size

    @property
    def size(self):
        '''Getter method to retrieve the value of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method to set the value of size'''
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Calculate the area of the square'''
        return self.__size**2
