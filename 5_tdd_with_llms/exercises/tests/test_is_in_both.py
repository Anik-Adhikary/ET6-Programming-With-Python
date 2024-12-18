import unittest

from ..is_in_both import is_item_in_both_lists
class test_is_in_both(unittest.TestCase):
  """To test the function is_item_in_both_lists"""

  def test_is_item_in_both_lists(self):
        """Test when item is in both lists, expected outcome is True"""
        list_a = ["king", "queen", "joker"]
        list_b = ["hearts", "joker", "spades"]
        
        result = is_item_in_both_lists("joker", list_a, list_b)
        self.assertTrue(result)

  def test_item_not_in_both_lists(self):
        """Test when item is not in both lists, expected outcome is False"""
        list_a = ["king", "queen", "jack"]
        list_b = ["diamonds", "hearts", "spades"]
    
        result = is_item_in_both_lists("joker", list_a, list_b)
        self.assertFalse(result) 

  def test_item_in_first_list_only(self):
        """Test when item is only in the first list, expected outcome is False"""
        list_a = ["king", "queen", "jack"]
        list_b = ["hearts", "ace", "spades"]

        result = is_item_in_both_lists("jack", list_a, list_b)
        self.assertFalse(result) 
        
  def test_item_in_second_list_only(self):
        """Test when item is only in the second list, expected outcome is False"""
        list_a = ["king", "queen", "jack"]
        list_b = ["hearts", "ace", "spades"]
        
        result = is_item_in_both_lists("ace", list_a, list_b)
        self.assertFalse(result)  





  