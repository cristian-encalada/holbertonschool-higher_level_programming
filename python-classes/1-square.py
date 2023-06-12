#!/usr/bin/python3
''' Task 1. Write a class Square that defines a square (based on 0-square.py)

    Requiremnts:
    -----------
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
    - Is not allowed to import any module

    Notes:
    -----
    Why size is private attribute?

    The size of a square is crucial for a square, many things depend of it
    (area computation, etc.), so, as class builder, must control the type
    and value of this attribute.
    One way to have the control is to keep it privately.
'''


class Square:
    '''Defines a square'''
    def __init__(self, size):
        '''Instantiation'''
        self.__size = size
