def array_subsets(a):
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
