def solve_me_first(a, b):
    """
    Return the sum of a and b

    Parameters:
    -----------
    a : int
        The first integer in the sum.
    b : int
        The second integer in the sum.

    Returns:
    --------
    int
        The sum of a and b.

    Examples:
    ---------
    >>> solve_me_first(2,3)
    5

    >>> solve_me_first(10, 15)
    15
    """
    return a + b

assert solve_me_first(2,3) == 5
assert solve_me_first(10, 15) == 25
assert solve_me_first(100, 1000) == 1100
