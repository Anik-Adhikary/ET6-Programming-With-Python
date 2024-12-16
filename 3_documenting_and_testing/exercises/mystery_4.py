def mystery_4(a):
    """Generates a lsit of sorted positive integers from 0 to a-1

    Parameters:
    - a(int): is the length of the lists to be generated, must be a non-negative integer.

    Returns:
    - A list containing positive integers from 0 to a-1

    Example:
    >>> mystery_4(8)
    [0,1,2,3,4,5,6,7]
    """
    # initialises an empty list
    b = []

    #  is initialised to 0 to track the next number to append
    c = 0
    while len(b) < a:
        # keeps appending `c`to `b` and increments `c` by 1 until the length of `b` equals `a`
        b.append(c)
        c = c + 1

    return b
