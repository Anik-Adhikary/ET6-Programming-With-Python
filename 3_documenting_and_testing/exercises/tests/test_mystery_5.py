import unittest

from ..mystery_5 import mystery_5

class TestMystery5(unittest.TestCase):
    """Test the mystery_5 function"""

    def test_letters_input(self):
        """"""
        self.assertEqual(mystery_5(['n','i','k','e'], []), ['e','i','k','n'])

    def test_letters_input(self):
        """"""
        self.assertEqual(mystery_5(['king','ace','queen','joker'], []), ['ace','joker','king','queen'])
        
    def test_letters_input(self):
        """"""
        self.assertEqual(mystery_5([3,1,4,1,5,9,2,6], []), [1,1,2,3,4,5,6,9])
        

   
