def array_hopscotch(a, i_start):
    """
    Play a game of 'array hopscotch'.

    The game is played as follows. Given an array 'a' containing integers
    greater than or equal to zero, and a starting index 'i_start', hop
    left and right in the array by the distance contained in a[i_start].
    Then repeat the process for the new elements you land on.

    Continue in this manner until you either land on a zero element
    (i.e. you win the game), or you realize that it is not possible to
    land on a zero element (i.e. you lose the game).

    We use a recursive algorithm to play the game, keeping track of
    elements we have visited. If we land on a zero, we win. If, regardless
    of whether we hop left or right, we land on an element we have already
    visited, then we are stuck in an infinite loop, and we lose.

    Since each element in the array is visited at most once, the execution
    time is O(n), worst case.

    :param a: The array in which we are to play our game of array hopscotch.
    :param i_start: The starting index for our game.
    :return: A set containing all the winning paths. Each winning path is a
    tuple containing a sequence of hop indices that lead to a zero element.
    If there are no winning paths, the set will be empty.
    """
    return _helper(a, i_start, set())


def _helper(a, i_start, visited):
    """
    Helper function to perform loop detection.

    :param a: (Same as in main function.)
    :param i_start: (Same as in main function.)
    :param visited: A set of indices that have already been visited during
    our game of array hopscotch. Do not continue to explore any paths that
    land on any of these indices.
    :return: (Same as in main function.)
    """
    result = set()
    # error checking
    if not isinstance(a, tuple) or not (0 <= i_start < len(a)) or a[i_start] < 0:
        return result
    # loop detection
    if i_start in visited:
        return result
    # base case
    if a[i_start] == 0:
        result.add((i_start,))
        return result

    # recursive step
    visited.add(i_start)  # don't revisit starting index
    for i_hop in (i_start - a[i_start], i_start + a[i_start]):
        remaining_paths = _helper(a, i_hop, visited)
        for path in remaining_paths:
            result.add((i_start,) + path)
    visited.remove(i_start)  # ok to revisit starting index

    return result
