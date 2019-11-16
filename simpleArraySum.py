import numpy as np
def simpleArraySum(ar):
    """
    Return the sum of all the elements in the array, a.

    Parameters
    ----------
    ar : a numpy array
        An array with the integer elements to sum.

    Returns
    --------
    int
        The sum of the integer elements within the array.

    Examples
    --------
    >>> my_array = np.array([1,2,3,4])
    >>> my_array2 = np.array([1,2,3,4,10,11])
    >>> simpleArraySum(my_array)
    10
    >>> simpleArraySum(my_array2)
    31
    """
    return np.sum(a)

assert simpleArraySum(np.array([1,2,3,4])) == 10
assert simpleArraySum(np.array([1,2,3,4,10,11])) == 31

# alternate solution without using numpy
def simpleArraySum2(ar):
    """
    Return the sum of all the elements in the array, a.

    Parameters
    ----------
    ar : a numpy array
        An array with the integer elements to sum.

    Returns
    --------
    int
        The sum of the integer elements within the array.

    Examples
    --------
    >>> my_array = np.array([1,2,3,4])
    >>> my_array2 = np.array([1,2,3,4,10,11])
    >>> simpleArraySum2(my_array)
    10
    >>> simpleArraySum2(my_array2)
    31
    """
    my_sum = 0
    for num in ar:
        my_sum += num
    return my_sum
