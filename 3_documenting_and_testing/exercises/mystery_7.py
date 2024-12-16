def mystery_7(a, b):
    """The function filters a sequence of elements by checking if each element contains the value`b`
    
    Parameters:
    - a(iterable): a sequence of elements to be checked
    - b(any): the value to check for within each element of `a`

    Returns:
    A new list containing elements from `a` that contains `b`

    Example:
    >>> mystery_7(['Homnelander', 'Soldierboy', 'Butcher'], 'o')
    ['Homelander','Butcher']
    """
    #`c` is initialised to store the new list
    c = []
    for d in a:
        if b in d:
            # all elements appends to a new list that is `c`
            c.append(d)
    return c
