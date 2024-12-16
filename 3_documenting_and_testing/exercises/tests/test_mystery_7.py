import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """Test the mystery_7 function"""

    def test_minimal_input_list(self):
        """"""
        self.assertEqual(mystery_7([], []), [])

    def test_minimal_input_string(self):
        """"""
        self.assertEqual(mystery_7('', ''), [])

    def test_Supes_input_string(self):
        """"""
        self.assertEqual(mystery_7(['Homnelander', 'Soldierboy', 'Butcher'], 'o'), ['Homelander','Butcher'])
