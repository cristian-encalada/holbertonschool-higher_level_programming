#!/usr/bin/python3
"""Task 9. Student to JSON
"""


class Student:
    """Define a student
    """
    def __init__(self, first_name, last_name, age):
        """Initialize the Student instance attributes (public)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance
        """
        return self.__dict__
