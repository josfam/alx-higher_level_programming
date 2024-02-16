#!/usr/bin/python3

"""Write the class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of this square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of this square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Human-readable representation of the Square"""
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return '[Square] ({}) {}/{} - {}'.format(id, x, y, size)
