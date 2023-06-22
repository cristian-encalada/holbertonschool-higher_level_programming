#!/usr/bin/python3
"""Task 6. Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Write an Object to a text file, using a JSON representation"""
    with open(filename, 'r') as json_file:
        return json.load(json_file)
