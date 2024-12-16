def mystery_6(a, b):
    """ It generates a list of length `a`, whwere the list starts with `b` and
    thereafter increases the value of `b` by 1 for each subsequent element.

    Parameters:
    - a(int): The number of elements in the output list
    - b(int): The starting value of the lsit

    Returns:
    A list containing `a` elements, starting from `b` and incrementig by 1 for each element

    Examples:
    >>> mystery_6(3, 3) 
    [3,4,5]
    
    """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
