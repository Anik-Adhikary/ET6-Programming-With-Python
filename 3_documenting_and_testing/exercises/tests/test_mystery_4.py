import unittest

from ..mystery_4 import mystery_4

class TestMystery4(unittest.TestCase):
    """Test the mystery_4 function"""

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_4(0), [])
    
    def test_minimal_input(self):
        """It should return 0,1,2,3,4,5,6,7"""
        self.assertEqual(mystery_4(8), [0,1,2,3,4,5,6,7])
