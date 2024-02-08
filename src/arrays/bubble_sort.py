def bubble_sort(a: tuple[int, ...]) -> None:
    """
    Sort an array using the bubble sort algorithm.

    The algorithm is optimized to avoid re-examining the already sorted
    elements that "sink" to the bottom of the array during each iteration.

    Performance is O(n*n).

    :param a: The array to be sorted. It will be sorted in place.
    :return: None
    """
    number_of_unsorted_elements = len(a)
    while number_of_unsorted_elements > 0:
        new_number_of_unsorted_elements = 0
        for i in range(number_of_unsorted_elements - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                new_number_of_unsorted_elements = i + 1
        number_of_unsorted_elements = new_number_of_unsorted_elements
