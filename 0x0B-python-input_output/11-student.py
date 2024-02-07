#!/usr/bin/python3

"""Write a class Student that defines a student"""


class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        new_dict = dict()
        if attrs and isinstance(attrs, list):
            for key in attrs:
                value = self.__dict__.get(key)
                if not value:  # skip a non-existent key
                    continue
                new_dict.update({key: value})
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        self.__dict__.update(json)
