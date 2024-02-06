#!/usr/bin/python3

"""
Write a function that writes a string to a text file (UTF8) and returns the
number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the
    number of characters written
    """
    chars_written = 0
    with open(filename, 'w', encoding='UTF-8') as f:
        chars_written = f.write(text)

    return chars_written
