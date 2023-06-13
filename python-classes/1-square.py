#!/usr/bin/python3
''' Task 1. Write a class Square that defines a square (based on 0-square.py)

    Requiremnts:
    -----------
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
    - Is not allowed to import any module
'''


class Square:
    '''Defines a square'''
    def __init__(self, size):
        '''Initialize the Square object with a given size'''
        self.__size = size
