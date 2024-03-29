#!/usr/bin/python3

"""
Write the first class Base:
"""

import json
import os
import csv


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

        if list_objs is None:
            pass
        else:
            # collect the dictionary representations of all objects
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())

        # write the dictionary strings to a file
        with open(file, 'w', encoding='utf-8') as f:
            dicts_str = cls.to_json_string(dict_list)
            f.write(dicts_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of the JSON string representation, json_string"""
        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes
        (from the provided dictionary) already set
        """
        if cls.__name__ == 'Rectangle':
            # create rectangle with default, temporary, width and height
            new_object = cls(1, 1)
        else:
            # create square with a temporary default size of 1
            new_object = cls(1)

        # populate the class, overriding defaults where necessary
        new_object.update(**dictionary)

        return new_object

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances after parsing then from a file"""
        file = '{}.json'.format(cls.__name__)
        instance_list = []

        if not os.path.exists(file):
            return []
        else:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    # skip empty lines
                    if line == '':
                        continue
                    else:
                        dict_list = cls.from_json_string(line)
                        for dictionary in dict_list:
                            instance_list.append(cls.create(**dictionary))

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and writes objects into a CSV file"""
        class_name = cls.__name__
        file = '{}.csv'.format(class_name)

        if class_name == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']
        # write object to csv file
        with open(file, 'w', encoding='utf-8') as f:
            for obj in list_objs:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a CSV file"""
        class_name = cls.__name__
        file = '{}.csv'.format(cls.__name__)
        instance_list = []

        if class_name == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']
        # read properties from the csv file
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for instance_info in reader:
                # turn string values in dict into integers
                for key, val in instance_info.items():
                    instance_info[key] = int(val)
                # create a new instance and add it to the list
                new_instance = cls.create(**instance_info)
                instance_list.append(new_instance)

        return instance_list
