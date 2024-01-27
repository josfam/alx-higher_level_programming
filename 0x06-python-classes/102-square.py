#!/usr/bin/python3

"""My first square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Returns the current area of the square"""
        return self.__size**2

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ "Sets the size of the square to the given value"""
        if not (isinstance(value, int)):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __eq__(self, other):
        """Checks if this square has an equal area as the other square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if this square does not have an equal area as the other
        square
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """Checks if this square has an area that is greater than
        the other square
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this square has an area that is greater than or equal
        to the other square
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Checks if this square has an area that is less than the
        other square
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this square has an area that is less than or equal
        to the other square
        """
        return self.area() <= other.area()
