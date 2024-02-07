def array_subsets(a: tuple[int, ...]) -> tuple[int, ...]:
    """
    Partitions an array `a` of integers into disjoint sub-arrays `arr_a`
    and `arr_b` such that `arr_a` is the smallest possible subarray whose
    elements sum to a greater number than the elements of `arr_b`. (Note
    that neither `arr_a` nor `arr_b` need consist of consecutive elements
    from `a`.)

    The strategy is to first sort the given array in descending order.
    Then, starting from the first element, keep adding elements to `arr_a`
    until the running total of the elements in `arr_a` exceeds the running
    total of the remaining elements (in `arr_b`).

    Performance is O(n*log(n)), due to the sorting operation.

    :param a: The array to be partitioned.
    :return: The subarray `arr_a`, with its elements in ascending order.
    """
    result = []
    if a is None or len(a) == 0:
        return ()
    a = list(a)
    a.reverse()
    sum_a = 0
    sum_b = sum(a)
    for n in a:
        result.append(n)
        sum_a += n
        sum_b -= n
        if sum_a > sum_b:
            break
    result.sort()
    return tuple(result)
