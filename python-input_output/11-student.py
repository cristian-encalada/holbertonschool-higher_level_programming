#!/usr/bin/python3
"""Task 11. Student to disk and reload
"""


class Student:
    """Define a student
    """
    def __init__(self, first_name, last_name, age):
        """Initialize the Student's instance attributes (public)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance
        """
        if type(attrs) is list:
            my_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance
        """
        for i in self.__dict__:
            if i in json:
                self.__dict__[i] = json[i]
