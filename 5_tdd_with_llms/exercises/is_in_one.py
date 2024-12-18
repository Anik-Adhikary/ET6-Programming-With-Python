""" Is in one

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _only one_ of the lists.

"""
def is_item_in_only_one_list(item: str, list1: list, list2: list) -> bool:
    """
    Check if the given item is present in only one of the lists.

    Parameters:
    - item (str): The item to check.
    - list1 (list): The first list of strings.
    -list2 (list): The second list of strings.

    Returns:
    True if the item is in only one of the lists, False otherwise.
    """
    # Check if the item is in one of the lists, but not both
    return (item in list1) != (item in list2)
