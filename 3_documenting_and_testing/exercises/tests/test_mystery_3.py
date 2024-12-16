import unittest

from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    """Test the mystery_3 function"""

    def test_minimal_input(self):
        """It should return 0"""
        self.assertEqual(mystery_3(0, 0), 0)
    
    def test_a_smaller_than_b_input(self):
        """It should return 3"""
        self.assertEqual(mystery_3(3, 9), 3)

    def test_b_smaller_than_a_input(self):
        """It should return 3"""
        self.assertEqual(mystery_3(9, 3), 3)

    def test_a_equals_b_input(self):
        """It should return 18"""
        self.assertEqual(mystery_3(9, 9), 18)

    def test_float_input(self):
        """It should return 9.1"""
        self.assertEqual(mystery_3(9.1, 9.2), 9.1)

    def test_float_and_integer_input(self):
        """It should return 2"""
        self.assertEqual(mystery_3(3.4, 2), 2)
