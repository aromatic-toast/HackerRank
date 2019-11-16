def a_very_big_sum(ar):
    my_sum = 0
    for num in ar:
        my_sum += num
    return my_sum

assert a_very_big_sum([1000000001,1000000002,1000000003,1000000004,1000000005]) == 5000000015


