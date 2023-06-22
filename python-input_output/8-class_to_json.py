#!/usr/bin/python3
"""Task 8. Class to JSON"""
import json


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    for JSON serialization of an object
    """
    return json.dumps(obj.__dict__)
