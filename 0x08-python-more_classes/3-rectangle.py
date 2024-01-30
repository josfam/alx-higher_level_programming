#!/usr/bin/python3

"""Simulates a simple rectangle"""


class Rectangle:
    """Represents a simple rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the rectangle's width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the rectangle's height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of the rectangle, by using #s"""
        to_print = []
        if self.height == 0 or self.width == 0:
            return ''
        for h in range(self.height):
            to_print.append(f"{'#' * self.width}")
            if h < self.height - 1:
                to_print.append('\n')

        return ''.join(to_print)
