import pytest
from src.arrays.bubble_sort import bubble_sort


@pytest.fixture(scope="session", autouse=True)
def before_session():
    print()
    print()
    print("=================")
    print("Test bubble_sort:")
    print("=================")


def test_array_with_one_element():
    a = [1]
    expected = [1]
    do_test(a, expected)


def test_already_sorted_array():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    do_test(a, expected)


def test_worst_case():
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    do_test(a, expected)


def test_average_case_1():
    a = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    do_test(a, expected)


def test_average_case_2():
    a = [4, 2, 3, 1, 7, 5, 10, 9, 8, 6]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    do_test(a, expected)


def do_test(a, expected):
    a_copy = a.copy()
    bubble_sort(a_copy)
    assert a_copy == expected
    print(f"\n\nbubbleSort([{','.join(map(str, a))}]) = [{','.join(map(str, a_copy))}]")
