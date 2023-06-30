#!/usr/bin/python3
"""Task 0. Base class
"""
import json


class Base:
    """Base class
    """
    __nb_objects = 0  # class attribute

    def __init__(self, id=None):
        """Class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            # ensure that each instance of the Base class has a unique id
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
