def mystery_3(a, b):
    """It compares two numbers and returns a value based on some conditions
    
        Parameters
        - a: int/float: first no.
        - b: int/float: second no.

        Examples:
        >>> mystery_3(3,9)
        3
        >>> mystery_3(9,3)
        3
        >>> mystery_3(9,9)
        18
    """
    # if a smaller than b, then a is returned
    if a < b:
        return a
    # if b smaller than a, then b is returned
    elif a > b:
        return b
    # if a equals b, then their sum is returned
    else:
        return a + b
