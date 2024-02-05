from src.arrays.array_subsets import array_subsets


def test_null_array():
    print()
    print()
    print("===================")
    print("Test array_subsets:")
    print("===================")

    a = None
    expected = []
    do_test(a, expected)


def test_empty_array():
    a = []
    expected = []
    do_test(a, expected)


def test_array_with_single_element():
    a = [1]
    expected = [1]
    do_test(a, expected)


def test_array_with_no_duplicate_elements():
    a = [1, 2, 3, 4]
    expected = [3, 4]
    do_test(a, expected)


def test_longer_array_with_no_duplicate_elements():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [7, 8, 9, 10]
    do_test(a, expected)


def test_array_with_some_duplicate_elements():
    a = [1, 2, 2, 3, 3, 3, 4]
    expected = [3, 3, 4]
    do_test(a, expected)


def test_array_with_all_duplicate_elements():
    a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected = [1, 1, 1, 1, 1, 1]
    do_test(a, expected)


def do_test(a, expected):
    actual = array_subsets(a)
    assert actual == expected
    print(f"a = {a}, arrA = {actual}")
