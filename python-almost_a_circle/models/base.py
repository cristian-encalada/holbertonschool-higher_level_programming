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

    @staticmethod
    def from_json_string(json_string):
        """Return the list of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            attributes = ["width", "height"]
        else:
            attributes = ["size"]

        new_instance = cls(*[dictionary.get(attr, 5) for attr in attributes])
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        file_to_read = f"{cls.__name__}.json"
        try:
            with open(file_to_read, 'r') as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                return [cls.create(**obj_dict) for obj_dict in dict_list]
        except FileNotFoundError:
            return []
