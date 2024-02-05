#!/usr/bin/python3

"""
0. Lookup:
Write a function that returns the list of available attributes and methods
of an object
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    object_attrs = set(object.__dict__)
    obj_attrs = set(obj.__dict__)
    return list(object_attrs.union(obj_attrs))
