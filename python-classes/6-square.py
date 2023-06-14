#!/usr/bin/python3
""" Task 6. Coordinates of a square

    Requirements:
    ------------
    - Write a class Square that defines a square by: (based on 5-square.py)

    - Private instance attribute: size:
        - property def size(self): to retrieve it
        - property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a TypeError exception
                with the message size must be an integer
            - if size is less than 0, raise a ValueError exception
                with the message size must be >= 0
    - Private instance attribute: position:
        - property def position(self): to retrieve it
        - property setter def position(self, value): to set it:
            - position must be a tuple of 2 positive integers,
                otherwise raise a TypeError exception with the message:
                position must be a tuple of 2 positive integers
    - Instantiation with optional size
         and optional position: def __init__(self, size=0, position=(0, 0)):
    - Public instance method: def area(self): returns the current square area
    - Public instance method: def my_print(self): that prints in stdout
            the square with the character #:
            - if size is equal to 0, print an empty line
            - position should be use by using space
            - Don't fill lines by spaces when position[1] > 0
    - Is not allowed to import any module
"""


class Square:
    """Define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method to retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the value of size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the value of position"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size**2

    def my_print(self):
        """Print in stdout a square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                if self.__position[1] > 0:
                    print()
            line = ' ' * self.__position[0] + '#' * self.__size
            """Print the square line by line"""
            for _ in range(self.__size):
                print(line)
