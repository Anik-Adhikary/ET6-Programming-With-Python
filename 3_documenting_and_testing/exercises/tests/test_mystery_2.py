import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """Test the mystery_2 function """

    def test_minimal_list_input(self):
        """It should return None"""
        self.assertEqual(mystery_2([]), None)

    def test_minimal_string_input(self):
        """It should return None"""
        self.assertEqual(mystery_2(''), None)

    def test_sorted_number_input(self):
        """It should return 5"""
        self.assertEqual(mystery_2([1,2,3,4,5]), 5)

    def test_unsorted_numbers_input(self):
        """It should return 6"""
        self.assertEqual(mystery_2([5,9,8,6,1,4]), 6)

    def test_unsorted_numbers_input(self):
        """It should return 3"""
        self.assertEqual(mystery_2([5.9,8.6,1.4]), 3)

    def test_minimal_string_input(self):
        """It should return 10"""
        self.assertEqual(mystery_2('Homelander'), 10)
