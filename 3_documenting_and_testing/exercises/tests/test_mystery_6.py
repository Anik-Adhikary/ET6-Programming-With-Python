import unittest

from ..mystery_6 import mystery_6

class TestMystery6(unittest.TestCase):
    """Test the mystery_6 function"""

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_6(0, 0), [])

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_6(3, 3), [3,4,5])

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_6(9, 5), [5,6,7,8,9,10,11,12,13])
