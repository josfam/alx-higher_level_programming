#!/usr/bin/python3

"""My first square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the current area of the square"""
        return self.__size**2

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square to the given value"""
        if not (isinstance(value, int)):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        x, y = value
        if x < 0 or y < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        square_size = self.size
        if square_size == 0:
            print()
        else:
            for i in range(square_size):
                print(' ' * self.position[0], end='')
                print('#' * square_size)
