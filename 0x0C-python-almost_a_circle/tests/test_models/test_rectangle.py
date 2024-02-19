#!/usr/bin/python3

import unittest

from models.base import Base as B
from models.rectangle import Rectangle as R

class TestRectangle(unittest.TestCase):
    """Test cases for a Rectangle class"""
    def setUp(self) -> None:
        """Code to run before each test"""
        B._Base__nb_objects = 0  # reset object counter

    def test_new_rectangles_require_both_width_and_height(self):
        height_missing = "TypeError: Rectangle.__init__() missing 1 \
            required positional argument: 'height'"
        missing_both = "TypeError: Rectangle.__init__() missing 2 required \
            positional arguments: 'width' and 'height'"
        with self.assertRaises(TypeError, msg=height_missing):
            r1 = R(1)
        with self.assertRaises(TypeError, msg=missing_both):
            r2 = R()

    def test_new_rectangles_have_increasing_ids(self):
        r1 = R(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = R(3, 4)
        self.assertEqual(r2.id, 2)

    def test_new_rectangles_have_default_x_and_y_of_0(self):
        r1 = R(1, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)


if __name__ == '__main__':
    unittest.main()