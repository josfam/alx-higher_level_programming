import unittest

from models.rectangle import Rectangle as R

class TestRectangle(unittest.TestCase):
    def test_new_rectangles_require_both_width_and_height(self):
        height_missing = "TypeError: Rectangle.__init__() missing 1 \
            required positional argument: 'height'"
        missing_both = "TypeError: Rectangle.__init__() missing 2 required \
            positional arguments: 'width' and 'height'"
        with self.assertRaises(TypeError, msg=height_missing):
            r1 = R(1)
        with self.assertRaises(TypeError, msg=missing_both):
            r2 = R()

if __name__ == '__main__':
    unittest.main()