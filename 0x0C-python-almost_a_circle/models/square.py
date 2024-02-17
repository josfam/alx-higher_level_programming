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

    def update(self, *args, **kwargs):
        """Assigns a value to each attribute from a list of arguments or
        keywords
        """
        # assign values from *args if they exist
        if args and len(args):
            args_order = ['id', 'size', 'x', 'y']

            for property, value in zip(args_order, args):
                exec('self.{} = {}'.format(property, value))
        else:
            # assign values from **kwargs
            for k, v in kwargs.items():
                exec('self.{} = {}'.format(k, v))

    def __str__(self):
        """Human-readable representation of the Square"""
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return '[Square] ({}) {}/{} - {}'.format(id, x, y, size)
