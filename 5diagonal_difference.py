# problem statement:
# https://www.hackerrank.com/challenges/diagonal-difference/problem

import numpy as np 

def diagonal_difference(n, arr):
    """
    Return the absolute difference of the sums of the diagonals of arr.

    Parameters
    ----------
    arr : (array)
        A 2D array.
    n : (int)
        The number of columns present in the array.

    Returns
    -------
    int
        The absolute value of the difference between the sums of the diagonals.

    Examples
    --------
    >>> my_array = [[11,2,4],[4,5,6],[10,8,-12]]
    >>> diagonal_difference(3, my_array)
    15
    """
    # get the left diagonal values 
    left_diag = []
    index = 0
    for row in arr:
        value = row[index]
        left_diag.append(value)
        index += 1

    # get the right diagonal values
    right_diag = []
    index = n - 1
    for row in arr:
        value = row[index]
        right_diag.append(value)
        index -= 1

    # get the absolute difference of sum of diagonals
    diff = np.sum(left_diag) - np.sum(right_diag)

    return abs(diff)

# Unit Tests
my_array = np.array([[11, 2, 4,], [4,5,6], [10, 8, -12]])
my_array2 = np.array([[1,2,3], [4,5,6], [9,8,9]])
my_array3 = (np.array([[1, 5, 6, 8],
                       [2, 8, 9, 10],
                       [1, 3, 4, 5],
                       [8, 11, 10, 13]]))
n = 3
n2 = 4
assert diagonal_difference(n=n, arr=my_array) == 15
assert diagonal_difference(n=n, arr=my_array2) == 2
assert diagonal_difference(n=n2, arr=my_array3) == 2