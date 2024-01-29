import pytest
from src.arrays.array_hopscotch import array_hopscotch


@pytest.fixture(scope="session")
def before_first_test():
    print()
    print("Test ArrayHopscotch:")
    print("===================")


@pytest.mark.parametrize(
    "a, i_start, expected",
    [
        ((), 0, set()),
        ((2, 3, 1, 0, 5), -1, set()),
        ((2, 3, 1, 0, 5), 5, set()),
        ((2, 3, 1, 0, 5), 0, {(0, 2, 3)}),
        ((2, 2, 2, 0, 0), 0, {(0, 2, 4)}),
        ((1, 1, 1, 3, 1, 2, 0, 3), 5, {(5, 3, 6), (5, 7, 4, 3, 6)}),
        ((4, 2, 0, 3, 1, 5, 0), 0, {(0, 4, 3, 6)}),
        ((5, 2, 1, 3, 0, 1, 2, 4, 1), 3, {(3, 0, 5, 4), (3, 0, 5, 6, 4), (3, 6, 4)}),
        ((2, 2, 2, 0, 2), 0, set()),
    ],
)
def test_array_hopscotch(before_first_test, a, i_start, expected):
    actual = array_hopscotch(a, i_start)
    assert are_sets_equal(expected, actual)
    print(f"{a}, start = {i_start}")
    print("Winning hops:")
    print_paths(actual)


def are_sets_equal(set1, set2):
    return set1 == set2


def print_paths(paths):
    print("{")
    for path in paths:
        print(f"\t[{', '.join(map(str, path))}]")
    print("}")
