#!/usr/bin/python3

"""
Write a function that returns True if the object is exactly an instance of the
specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module
"""


def is_same_class(obj, a_class):
    """Return True if the provided object, obj, is exactly an instance of
    the specified class. Returns False otherwise
    """
    class_name = a_class.__name__
    obj_class_name = str(type(obj)).lstrip("<class ").rstrip(">").strip("'")
    return class_name == obj_class_name
