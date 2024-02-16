#!/usr/bin/python3

"""Write the class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """Human-readable representation of the Square"""
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return '[Square] ({}) {}/{} - {}'.format(id, x, y, size)
