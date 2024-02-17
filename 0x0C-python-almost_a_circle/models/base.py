#!/usr/bin/python3

"""
Write the first class Base:
"""

import json


class Base:
    """Represents the "base" of all other classes in the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"""
        if (list_dictionaries is None) or (not len(list_dictionaries)):
            return "[]"
        return json.dumps(list_dictionaries)
