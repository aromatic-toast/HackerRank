# Problem statement here: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
from  math import floor

def sockMerchant(n, ar):
    """
    Produce the number of matching pairs of socks available in ar.

    Parameters
    ----------
    n : (int) The number of socks in the pile.
    ar : (list) A list of ints where each unique int is different sock color.

    Returns
    -------
    int : The total number of matching paris of socks contained in ar.

    Examples
    --------
    >>> sockMerchant(n=7, ar=[1,2,1,21,3,2])
    >>> 2
    >>> sockMerchant(n=9, ar=[10, 20, 20, 10, 10, 30, 50, 10, 20])
    >>> 3
    >>> sockMerchant(n=1, ar=[1])
    >>> 0
    """
    # check if n >= 2 or ar is too short
    if n < 2 or len(ar) < 2:
        return 0
    # initialize sock_dict
    sock_dict = {}

    for sock in ar:
        try:
            # add to sock count if sock already a key
            sock_dict[sock] += 1
        except:
            # set initial count of sock when its a new key
            sock_dict[sock] = 1

    # get number of matching pairs
    pairs = 0
    for sock, count in sock_dict.items():
        if count % 2 == 0:
            pairs += int(count / 2)
        else:
            pairs += int(floor(count / 2))

    return pairs

assert sockMerchant(n=7, ar=[1,2,1,21,3,2]) == 2
assert sockMerchant(n=9, ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
assert sockMerchant(n=1, ar=[1]) == 0





