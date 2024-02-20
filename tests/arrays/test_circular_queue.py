import pytest
from src.arrays.circular_queue import CircularQueue

queue = CircularQueue(10)


@pytest.fixture(scope="session", autouse=True)
def before_session():
    print()
    print()
    print("====================")
    print("Test circular_queue:")
    print("====================")


def test_add_and_remove():
    # add five elements
    print()
    add(1)
    add(2)
    add(3)
    add(4)
    add(5)

    # remove three elements
    print()
    for i in range(3):
        element = remove()
        assert element == i + 1

    # add five more elements
    print()
    add(6)
    add(7)
    add(8)
    add(9)
    add(10)

    # remove two more elements
    print()
    for i in range(2):
        element = remove()
        assert element == i + 4

    # add five more elements
    print()
    add(11)
    add(12)
    add(13)
    add(14)
    add(15)

    # try to add one more element (should fail -- queue full)
    print()
    assert not add(16)

    # remove three more elements
    print()
    for i in range(3):
        element = remove()
        assert element == i + 6

    # add three more elements
    print()
    add(17)
    add(18)
    add(19)

    # try to add one more element (should fail -- queue full)
    print()
    assert not add(20)

    # remove seven elements
    print()
    for i in range(7):
        element = remove()
        assert element == i + 9

    # remove three more elements
    print()
    for i in range(3):
        element = remove()
        assert element == i + 17

    # try to remove another element (should fail - queue empty)
    print()
    element = remove()
    assert element is None


def add(element):
    success = queue.add(element)
    outcome = "success" if success else "FAILED (queue full)"
    print(f"Adding element {element} ... {outcome}")
    return success


def remove():
    result = queue.poll()
    outcome = "FAILED (queue empty)" if result is None else str(result)
    print(f"Removing element {outcome}")
    return result
