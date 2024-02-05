#!/usr/bin/python3

"""1. My list
Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but
sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module
"""


class MyList(list):
    """A subclass of list, that can print a sorted list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints the list, but in sorted order (from smallest to biggest)"""
        list_copy = super().copy()
        print(sorted(list_copy))
