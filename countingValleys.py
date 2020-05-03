def countingValleys(n, s):
    """
    Produce the number of valleys traversed.
    Parameters
    ----------
    n : (int) The number of steps in the hike.
    s : (string) A string of length n, describing the steps in Gary's path.
    Returns
    -------
    int : Returns an integer representing the number of valleys traversed in s.

    Examples
    --------
    >>> countingValleys(n=8, s="UDDDUDUU")
    >>> 1
    """
    # keep track of altitude position on hike
    altitude = 0
    valley_count = 0
    for step in range(n):

        # check if returning to sea-level from a valley
        if altitude < 0 and s[step] == "U" and altitude + 1 == 0:
            valley_count += 1

        # update the altitude position
        if s[step] == "U":
            altitude += 1
        if s[step] == "D":
            altitude -= 1

    return valley_count

assert countingValleys(n=8, s="UDDDUDUU") == 1
