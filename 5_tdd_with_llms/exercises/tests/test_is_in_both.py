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
        """"""
        list_a = ["king", "queen", "jack"]
        list_b = ["diamonds", "hearts", "spades"]
        
        # Test when item is not in both lists
        result = is_item_in_both_lists("joker", list_a, list_b)
        self.assertFalse(result) 

  def test_item_not_in_both_lists(self):
        list_a = ["apple", "banana", "cherry"]
        list_b = ["banana", "cherry", "date"]
        
        # Test when item is not in both lists
        result = is_item_in_both_lists("apple", list_a, list_b)
        self.assertFalse(result)  # Expected outcome is False

  def test_item_in_first_list_only(self):
        list_a = ["apple", "banana", "cherry"]
        list_b = ["banana", "cherry", "date"]
        
        # Test when item is only in the first list
        result = is_item_in_both_lists("apple", list_a, list_b)
        self.assertFalse(result)  # Expected outcome is False
        
  def test_item_in_second_list_only(self):
        list_a = ["apple", "banana", "cherry"]
        list_b = ["banana", "cherry", "date"]
        
        # Test when item is only in the second list
        result = is_item_in_both_lists("date", list_a, list_b)
        self.assertFalse(result)  # Expected outcome is False





  