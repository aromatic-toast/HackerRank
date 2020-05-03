import numpy as np

def compareTriplets(a,b):
    """
    Return the comparison scores of a and b.

    Parameters
    ----------
    a : array
        An array of HackerRank review scores for Alice
    b : array
        An array of HackerRank review scores for Bob

    Returns
    -------
    array
        An array of the respective comparison points earned by Alice and then Bob.

    Examples
    --------
    alice = np.array([5,6,7])
    bob = np.array([3,6,10])
    >>> compareTriplets(alice, bob)
    np.array([1,1])
    """
    alice_scores = np.zeros(3, dtype=int)
    bob_scores = np.zeros(3, dtype=int)

    for score in range(len(a)):
        if a[score] > b[score]:
            alice_scores[score] += 1
        if b[score] > a[score]:
            bob_scores[score] += 1
    alice_score = np.sum(alice_scores)
    bob_score = np.sum(bob_scores)

    return np.array([alice_score,bob_score])

assert np.array_equal(compareTriplets(np.array([5,6,7]),np.array([3,6,10])), np.array([1,1]))
assert np.array_equal(compareTriplets(np.array([17,28,30]), np.array([99,16,8])), np.array([2,1]))


# solution without using numpy

def compareTriplets2(a,b):
    """
    Return the comparison scores of a and b.

    Parameters
    ----------
    a : list
        A list of HackerRank review scores for Alice
    b : list
        A list of HackerRank review scores for Bob

    Returns
    -------
    array
        A list of the respective comparison points earned by Alice and then Bob.

    Examples
    --------
    alice = [5,6,7]
    bob = [3,6,10]
    >>> compareTriplets2(alice,bob)
    [1,1]
    """
    alice_scores = [0,0,0]
    bob_scores = [0,0,0]

    for score in range(len(a)):
        if a[score] > b[score]:
            alice_scores[score] += 1
        if b[score] > a[score]:
            bob_scores[score] += 1
    alice_score = sum(alice_scores)
    bob_score = sum(bob_scores)

    return [alice_score,bob_score]

assert set(compareTriplets2([5,6,7],[3,6,10])) == set([1,1])
assert set(compareTriplets2([17,28,30], [99,16,8])) == set([2,1])



