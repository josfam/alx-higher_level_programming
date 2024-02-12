#!/usr/bin/python3

"""Write the class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        self.__height = value

    @property
    def y(self):
        """Returns the y value for this rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value for this rectangle"""
        self.__y = value

    @property
    def x(self):
        """Returns the x value for this rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value for this rectangle"""
        self.__x = value
