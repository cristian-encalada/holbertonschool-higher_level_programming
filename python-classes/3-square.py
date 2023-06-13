#!/usr/bin/python3
''' Task 3. Area of a square

    Requirements:
    ------------
    - Write a class Square that defines a square (based on 2-square.py)

    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0):
        - size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
        - if size is less than 0, raise a ValueError exception
            with the message size must be >= 0
    - Public instance method: def area(self): returns the current square area
    - Is not allowed to import any module
'''


class Square:
    '''Defines a square'''
    def __init__(self, size=0):
        '''Initialize the Square object with a given size (default = 0)'''
        self.__size = size

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Calculate the area of the square'''
        return self.__size**2
