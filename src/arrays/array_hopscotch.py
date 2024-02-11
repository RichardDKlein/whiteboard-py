def array_hopscotch(a: tuple[int, ...], i_start: int) -> set[tuple[int, ...]]:
    """
    Play a game of "array hopscotch".

    The game is played as follows. Given an array 'a' containing integers
    greater than or equal to zero, and a starting index 'iStart', hop left
    or right in the array by the distance contained in a[iStart]. Then repeat
    the hopping process for the new element you land on: Hop left or right by
    the distance contained in that new element.

    There are two important restrictions on the hopping process:

    (1) If a hop would take you beyond the bounds of the array, that is not
    a legal hop; and

    (2) If a hop would take you to an element you have already visited, that
    is not a legal hop.

    Continue in this manner until you either land on a zero element (i.e., you
    win the game), or you land on an element from which there are no legal hops
    (i.e., you lose the game).

    We shall use a recursive algorithm to play the game, keeping track of the
    elements we have visited.

    Since each element in the array is visited at most once, the execution time
    is O(n), worst case.</p>

    :param a: The array in which we are to play our game of array hopscotch.
    :param i_start: The starting index for our game.
    :return: A set containing all the winning paths. Each winning path is a
    tuple containing a sequence of unique hop indices that lead to a zero
    element. If there are no winning paths, the set will be empty.
    """
    return _helper(a, i_start, set())


def _helper(
    a: tuple[int, ...], i_start: int, visited: set[int]
) -> set[tuple[int, ...]]:
    """
    Helper function to perform loop detection.

    :param a: (Same as in main function.)
    :param i_start: (Same as in main function.)
    :param visited: A set of indices that have already been visited during
    our game of array hopscotch. Do not continue to explore any paths that
    land on any of these indices.
    :return: (Same as in main function.)
    """
    # error checking
    if not isinstance(a, tuple) or not (0 <= i_start < len(a)) or a[i_start] < 0:
        return set()
    # loop detection
    if i_start in visited:
        return set()
    # base case
    if a[i_start] == 0:
        result = set()
        result.add((i_start,))
        return result

    # recursive step
    result = set()
    visited.add(i_start)  # don't revisit starting index
    for i_hop in (i_start - a[i_start], i_start + a[i_start]):
        remaining_paths = _helper(a, i_hop, visited)
        for path in remaining_paths:
            result.add((i_start,) + path)
    visited.remove(i_start)  # ok to revisit starting index
    return result
