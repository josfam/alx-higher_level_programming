#!/usr/bin/python3

import unittest

from models.base import Base as B
from models.square import Square as S
from models.rectangle import Rectangle as R

class TestSquare(unittest.TestCase):
    
    """Test cases for a Rectangle class"""       

    # store various error messages
    errors = {
        'size_missing':"TypeError: Square.__init__() missing 1 required\
                positional argument: 'size'",
        'width_limit': 'width must be > 0',
    }

    def setUp(self) -> None:
        """Code to run before each test"""
        B._Base__nb_objects = 0  # reset object counter for every test
    
    def test_squares_must_inherit_from_Rectangle(self):
        parent = S.__base__.__name__
        self.assertEqual(parent, 'Rectangle')

    def test_a_new_square_requires_a_size(self):
        with self.assertRaises(TypeError, msg=self.errors['size_missing']):
            s1 = S()

    def test_new_squares_have_increasing_ids(self):
        s1 = S(1)
        self.assertEqual(s1.id, 1)
        s2 = S(10)
        self.assertEqual(s2.id, 2)

    def test_new_squares_have_default_x_and_y_of_0(self):
        s1 = S(10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_invalid_size_uses_rectangles_error_checking(self):
        with self.assertRaises(ValueError, msg=self.errors['width_limit']):
            s1 = S(0)
            s2 = S(10)
            s2.size = 0

    def test_setting_size_changes_that_value(self):
        s1 = S(10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        s1.size = 20
        self.assertEqual(s1.width, 20)
        self.assertEqual(s1.width, 20)
