import unittest

from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S

class TestBase(unittest.TestCase):
    def test_new_Base_objects_increment_ids_by_1(self):
        base_1 = B()
        base_2 = B()
        self.assertEqual(base_2.id, 2)

if __name__ == '__main__':
    unittest.main()
