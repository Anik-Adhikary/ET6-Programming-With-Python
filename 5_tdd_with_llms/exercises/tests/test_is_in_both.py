import unittest

from ..is_in_both import is_item_in_both_lists
class test_is_in_both(unittest.TestCase):
  """"""

  def test_is_item_in_both_lists(self):
        """"""
        list_a = ["king", "queen", "joker"]
        list_b = ["hearts", "joker", "spades"]
        
        # Test when item is in both lists
        result = is_item_in_both_lists("joker", list_a, list_b)
       
        self.assertTrue(result)  # Expected outcome is True

  def test_item_not_in_both_lists(self):
        list_a = ["king", "queen", "jack"]
        list_b = ["diamonds", "hearts", "spades"]
        
        # Test when item is not in both lists
        result = is_item_in_both_lists("joker", list_a, list_b)
        self.assertFalse(result) 





  