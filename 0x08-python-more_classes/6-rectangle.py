#!/usr/bin/python3

"""Simulates a simple rectangle"""


class Rectangle:
    """Represents a simple rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """Returns the canonical representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Displays a deletion message if this rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
