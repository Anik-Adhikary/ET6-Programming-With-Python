import unittest

from ..is_in_one import is_item_in_only_one_list
class test_is_in_both(unittest.TestCase):
  """"""
  def test_item_in_only_first_list(self):
        """"""
        list_a = ["king", "queen", "joker"]
        list_b = ["diamonds", "hearts", "spades"]
        
        # Test when item is only in the first list
        result = is_item_in_only_one_list("joker", list_a, list_b)
        self.assertTrue(result)  # Expected outcome is True

  def test_item_in_only_second_list(self):
        """"""
        list_a = ["king", "queen", "joker"]
        list_b = ["diamonds", "hearts", "spades"]
        
        # Test when item is only in the second list
        result = is_item_in_only_one_list("spades", list_a, list_b)
        self.assertTrue(result)  # Expected outcome is True
  
  def test_item_in_neither_list(self):
        """"""
        list_a = ["king", "queen", "jack"]
        list_b = ["joker", "hearts", "spades"]
        
        # Test when item is not in either list
        result = is_item_in_only_one_list("ace", list_a, list_b)
        self.assertFalse(result)  # Expected outcome is False
