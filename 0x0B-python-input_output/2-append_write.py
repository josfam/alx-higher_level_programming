#!/usr/bin/python3

"""
Write a function that appends a string at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    with open(filename, 'a', encoding='UTF-8') as f:
        chars_written = f.write(text)
    return chars_written
