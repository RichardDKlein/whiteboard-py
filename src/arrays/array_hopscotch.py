def array_hopscotch(a: tuple[int], i_start: int) -> set[tuple[int]]:
    """
    Play a game of 'array hopscotch'.

    The game is played as follows. Given an array 'a' containing integers
    greater than or equal to zero, and a starting index 'i_start', hop
    left and right in the array by the distance contained in a[iStart]. Then
    repeat the process for the new elements you land on.

    Continue in this manner until you either land on a zero element
    (i.e. you win the game), or you realize that it is not possible to
    land on a zero element (i.e. you lose the game).

    We use a recursive algorithm to play the game, keeping track of
    elements we have visited. If we land on a zero, we win. If, regardless
    of whether we hop left or right, we land on an element we have already
    visited, then we are stuck in an infinite loop, and we lose.

    Since each element in the array is visited at most once, the execution
    time is O(n), worst case.

    Args:
        a: The array in which we are to play "array hopscotch".
        i_start: The starting index for our game of hopscotch.

    Returns:
        A set containing all the winning paths. Each winning path is a tuple
        containing a sequence of hop indices that lead to a zero element.
        If there are no winning paths, the set will be empty.
    """
    visited = set()
    return _array_hopscotch_with_loop_detection(a, i_start, visited)


def _array_hopscotch_with_loop_detection(
    a: tuple[int], i_start: int, visited: set
) -> set[tuple[int]]:

    result = set()

    # error checking
    if not isinstance(a, tuple) or i_start < 0 or i_start >= len(a) or a[i_start] < 0:
        return result

    # base case
    hop = a[i_start]
    if hop == 0:
        result.add((i_start,))
        return result

    # recursive step
    visited.add(i_start)  # don't revisit starting index
    i_hop_left = i_start - hop
    if i_hop_left >= 0 and i_hop_left not in visited:
        remaining_paths = _array_hopscotch_with_loop_detection(a, i_hop_left, visited)
        for path in remaining_paths:
            new_path = (i_start,) + path
            result.add(new_path)

    i_hop_right = i_start + a[i_start]
    if i_hop_right < len(a) and i_hop_right not in visited:
        remaining_paths = _array_hopscotch_with_loop_detection(a, i_hop_right, visited)
        for path in remaining_paths:
            new_path = (i_start,) + path
            result.add(new_path)

    visited.remove(i_start)  # ok to revisit starting index

    return result
