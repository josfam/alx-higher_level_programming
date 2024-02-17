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
        """Returns the JSON string representation of list_dictionaries"""
        if (list_dictionaries is None) or (not len(list_dictionaries)):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        dict_list = []
        file = '{}.json'.format(cls.__name__)

        # collect the dictionary representations of all objects
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())

        # write the dictionary strings to a file
        with open(file, 'w', encoding='utf-8') as f:
            dicts_str = cls.to_json_string(dict_list)
            f.write(dicts_str)
