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
        if not isinstance(value, int):
            raise TypeError('width must be and integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Returns the x value for this rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value for this rectangle"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Returns the y value for this rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value for this rectangle"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints to stdout, the rectangle instance with #s, taking care of
        the x and y co-ordinates as well
        """
        x, y = self.x, self.y

        for h in range(y):  # move vertically
            print()
        for w in range(self.height):  # move horizontally
            print('{}{}'.format(' ' * x, '#' * self.width))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        original_dict = self.__dict__
        keys = self.__dict__.keys()

        # skip **kwargs if *args exists and is not empty
        if args and len(args):
            new_pairs = dict(zip(keys, args))
            original_dict.update(new_pairs)
        else:
            # translating the provided kwargs into class properties
            kwargs_translation = {
                'id': 'id',
                'width': '_Rectangle__width',
                'height': '_Rectangle__height',
                'x': '_Rectangle__x',
                'y': '_Rectangle__y'
            }

            for k, v in args.items():
                original_dict.update({kwargs_translation[k]: v})

    def __str__(self):
        """The more human-readable version of the Rectangle"""
        id = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return f'[Rectangle] ({id}) {x}/{y} - {w}/{h}'
