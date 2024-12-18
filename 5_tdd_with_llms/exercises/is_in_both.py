""" Is in Both

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _both_ of the lists.

"""
def is_item_in_both_lists(item: str, list1: list, list2: list) -> bool:
      """
    The function checks if the given item is present in both the lists.

    Parameters:
        item (str): The item to check.
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        bool: True if the item is in both lists, False otherwise.
    """
      return item in list1 and item in list2
# returns the result of the condition. If item exists in both lists, it returns True, otherwise it returns False.
