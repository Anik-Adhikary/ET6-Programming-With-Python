""" Sum Evens and Odds

Write a function that takes a list of numbers 
and returns a dictionary with sums of the even and odd numbers in the list.

"""
def sum_even_odd(numbers: list) -> dict:
    """This function takes a list of numbers and returns a dictionary with 
    sums of the even and odd numbers in the list.
    
    Parameters:
    - numbers (list): A list of integers to test the function with.
        
    Returns:
    - the result is verified using self.assertEqual
    """
    
    result = {'even': 0, 'odd': 0}
    
    for num in numbers:
        # for even numbers
        if num % 2 == 0:
            result['even'] += num

        # for odd numbers 
        else:
            result['odd'] += num

    return result
