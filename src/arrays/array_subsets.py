def array_subsets(a):
    """
    Partitions an array `a` of integers into disjoint sub-arrays `arrA`
    and `arrB` such that `arrA` is the smallest possible subarray whose
    elements sum to a greater number than the elements of `arrB`. (Note
    that neither `arrA` nor arrB` need consist of consecutive elements
    from `a`.)

    The strategy is to first sort the given array in descending order.
    Then, starting from the first element, keep adding elements to `arrA`
    until the running total of the elements in `arrA` exceeds the running
    total of the remaining elements (in `arrB`).

    Performance is O(n*log(n)), due to the sorting operation.

    :param a: The array to be partitioned.
    :return: The subarray `arrA`, with its elements in ascending order.
    """
    result = []
    if a is None or len(a) == 0:
        return result
    a.sort(reverse=True)
    sum_a = 0
    sum_b = sum(a)
    for n in a:
        result.append(n)
        sum_a += n
        sum_b -= n
        if sum_a > sum_b:
            break
    result.sort()
    return result
