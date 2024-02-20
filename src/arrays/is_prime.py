def is_prime(n: int) -> bool:
    """
    Determine whether a given positive integer is prime.

    :param n: A positive integer.
    :return: `True` if `n` is prime, `False` otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
