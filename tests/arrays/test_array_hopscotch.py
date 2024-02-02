from src.arrays.array_hopscotch import array_hopscotch


def test_empty_array():
    print()
    print()
    print("===================")
    print("Test ArrayHopscotch:")
    print("===================")

    a = ()
    i_start = 0
    expected = set()
    do_test(a, i_start, expected)


def test_start_index_too_small():
    a = (2, 3, 1, 0, 5)
    i_start = -1
    expected = set()
    do_test(a, i_start, expected)


def test_start_index_too_large():
    a = (2, 3, 1, 0, 5)
    i_start = 5
    expected = set()
    do_test(a, i_start, expected)


def test_start_index_already_wins():
    a = (2, 3, 1, 0, 5)
    i_start = 3
    expected = {(3,)}
    do_test(a, i_start, expected)


def test_one_winning_path_case_1():
    a = (2, 3, 1, 0, 5)
    i_start = 0
    expected = {(0, 2, 3)}
    do_test(a, i_start, expected)


def test_one_winning_path_case_2():
    a = (2, 2, 2, 0, 0)
    i_start = 0
    expected = {(0, 2, 4)}
    do_test(a, i_start, expected)


def test_one_winning_path_case_3():
    a = (4, 2, 0, 3, 1, 5, 0)
    i_start = 0
    expected = {(0, 4, 3, 6)}
    do_test(a, i_start, expected)


def test_two_winning_paths():
    a = (1, 1, 1, 3, 1, 2, 0, 3)
    i_start = 5
    expected = {(5, 3, 6), (5, 7, 4, 3, 6)}
    do_test(a, i_start, expected)


def test_three_winning_paths():
    a = (5, 2, 1, 3, 0, 1, 2, 4, 1)
    i_start = 3
    expected = {(3, 0, 5, 4), (3, 0, 5, 6, 4), (3, 6, 4)}
    do_test(a, i_start, expected)


def test_no_solution():
    a = (2, 2, 2, 0, 2)
    i_start = 0
    expected = set()
    do_test(a, i_start, expected)


def do_test(a, i_start, expected):
    actual = array_hopscotch(a, i_start)
    assert actual == expected
    print(f"\n\n{a}, start = {i_start}")
    print("Winning hops:")
    print_paths(actual)


def print_paths(paths):
    print("{")
    for path in paths:
        print(f"\t[{', '.join(map(str, path))}]")
    print("}")
