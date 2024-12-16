def mystery_2(a):
    """It returns the length of the input list, either no. or string
     Parameters:
     - a: no.(int/float) or string whose length is to be found

     Example:
     >>> mystery_2('Homelander')
    [10]
    """

    if len(a) == 0:
        return None
    # returns length of the input if it is not empty
    # returns None if the input is empty
    return len(a)
