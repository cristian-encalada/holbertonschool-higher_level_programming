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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        file_to_write = f"{cls.__name__}.json"

        dict_list = [obj.to_dictionary() for obj in list_objs] \
            if list_objs else []

        to_write = cls.to_json_string(dict_list)

        with open(file_to_write, 'w') as file_to_write:
            file_to_write.write(to_write)
