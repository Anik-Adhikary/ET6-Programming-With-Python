import unittest

from ..sum_evens_and_odds import sum_even_odd
class test_sum_evens_and_odds(unittest.TestCase):
  """To test the function sum_even_odd"""
  
  def test_sorted_odd_and_even_numbers(self):
        """Taking a sorted list of numbers, expected result-> even: 30, odd: 25"""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = {'even': 30, 'odd': 25}
       
        result = sum_even_odd(numbers)
        self.assertEqual(result, expected_result) # Check if the result matches the expected

  def test_unsorted_odd_and_even_numbers(self):
        """Taking an unsorted list of numbers, expected result-> even: 62, odd: 46"""
        numbers = [11,9,1,14,8,13,16,5,24,7]
        expected_result = {'even': 62, 'odd': 46}
       
        result = sum_even_odd(numbers)
        self.assertEqual(result, expected_result) # Check if the result matches the expected



  
