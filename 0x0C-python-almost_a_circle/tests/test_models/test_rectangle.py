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
        
    def test_setting_x_and_y_changes_those_values(self):
        r1 = R(1, 2, 3, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        r1.x = 4
        r1.y = 5
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_setting_width_and_height_changes_those_values(self):
        r1 = R(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        r1.width = 20
        r1.height = 30
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
    
    def test_invalid_types_for_width_and_height_report_errors(self):
        width_mismatch = 'width must be an integer'
        height_mismatch = 'height must be an integer'
       
        with self.assertRaises(TypeError, msg=width_mismatch):
            r1 = R('1', 2)
            r1 = R([], 2)
        with self.assertRaises(TypeError, msg=height_mismatch):
            r2 = R(1, '2')
            r2 = R(1, {})

    def test_invalid_types_for_x_and_y_report_errors(self):
        x_mismatch = 'x must be an integer'
        y_mismatch = 'y must be an integer'
        with self.assertRaises(TypeError, msg=x_mismatch):
            r1 = R(1, 2, {3})
        with self.assertRaises(TypeError, msg=y_mismatch):
            r1 = R(1, 2, 3, [4])

if __name__ == '__main__':
    unittest.main()
