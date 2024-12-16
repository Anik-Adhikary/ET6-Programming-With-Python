def mystery_5(a, b=None):
    """This function sorts a lists of strings or numbers
    - Strings are sorted by UNICODE value
    - Numbers are sorted in ascending order

    Examples:
    >>> mystery_5(['n','i','k','e'],[])
    ['e','i','k','n']

    >>> mystery_5([3,1,4,1,5,9,2,6],[])
    [1,1,2,3,4,5,6,9]
    """
    # makes sure there is a list to  fill
    if b is None:
    # moves items from one list to another in sorted order
        b = []
    while a:
        # finds the lowest item in the first list
        c = min(a)
        # moves it to the second list
        a.remove(c)
        b.append(c)
    return b
