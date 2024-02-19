def find_primes(n: int) -> [int]:
    """
    Find all primes up to a given integer.

    Our algorithm is the Sieve of Eratosthenes. We use an array 'isPrime'
    to keep track of which integers are prime: `isPrime[i]` = `True` if
    and only if 'i' is prime.

    All elements of `isPrime` are initialized to `True`, since as far as
    we know at the outset, all positive integers are prime.

    We then loop through the `isPrime` array, from `i` = 2` to the square
    root of `n`. If `isPrime[i]` is `True`, we mark all multiples of `i`
    as composite (i.e., non-prime). We do this by setting `isPrime[m * i]`
    to `False` for each multiple of `i`. Here, we take advantage of the
    following optimization: We need not start from `m` = 2; instead, we
    can start from `m` = `i`.

    To see why this is true, suppose that `m < i`. Now, `m` has a prime
    factorization `p1 * p2 * ... * pN`, where `pI <= m < i` for each of
    the prime factors `pI`. In particular, `p1 < i`. But that means that
    `isPrime[m * i]` = `isPrime[p1 * (p2 * ... * pN * i)]` has ALREADY
    been set to `True`. Why? Because, earlier in the loop through the
    `isPrime` array, we found that `p1` was prime, and therefore we
    marked all multiples of `p1` as composite.

    :param n: A positive integer.
    :return: An array containing all primes up to and including `n`.
    """
    primes = [True] * (n + 1)
    sqrt_n = int(n**0.5)
    for i in range(2, sqrt_n + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]
