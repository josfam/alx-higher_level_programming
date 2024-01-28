#!/usr/bin/python3

"""Addition of integers, a and b"""


def add_integer(a, b=98):
    """Adds two integers a and b, that can also be passed as floats"""
    if not (isinstance(a, (int, float))):
        raise TypeError('a must be an integer')
    elif not (isinstance(b, (int, float))):
        raise TypeError('b must be an integer')
    a, b = int(a), int(b)
    return a + b
