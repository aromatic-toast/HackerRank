def jumpingOnClounds(c):
    """
    Produce smallest number of jumps it takes to get from start of c to end.
    Parameters
    ----------
    c : (array) An array of clouds represented by binary integers.

    Returns
    -------
    int : The smallest number of safe jumps possible in c.

    Examples
    --------
    >>> jumpingOnClounds(c=[0,0,1,0,0,1,0])
    >>> 4
    >>> jumpingOnClounds(c=[0,0,0,0,1,0])
    >>> 3
    >>> jumpingOnClounds(c=[0,0,0,1,0,0])
    >>> 3
    """
    jumps = 0
    landing_pad = 0

    for index in range(len(c)):
        # check if index has already been jumped over
        if index < landing_pad:
            continue
        # check that index jump of 2 is within bounds
        if index < len(c) - 2:
            # check if jump of 2 is safe
            if c[index] == 0 and c[index + 2] == 0:
                jumps += 1
                landing_pad = index + 2
                continue

        # check that index jump of 1 is within bounds
        if index < len(c) - 1:
            # check if jump of 1 is safe
            if c[index] == 0 and c[index + 1] == 0:
                jumps += 1
                landing_pad = index + 1

    return jumps


assert jumpingOnClounds(c=[0,0,1,0,0,1,0]) == 4
assert jumpingOnClounds(c=[0,0,0,0,1,0]) == 3
assert jumpingOnClounds(c=[0,0,0,1,0,0]) == 3





