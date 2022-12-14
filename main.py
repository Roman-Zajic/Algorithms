"""-----------------------------------------------------------------

The library contains common algorithms and data structure examples.

Title:          Most Common Algorithms
Author:         Roman Zajic
Last modified:  2022-12-11

-----------------------------------------------------------------"""

import random
import search
import sort

def test_search(algorithm, element, array):
    result = algorithm(element, array)
    return result

def test_sort(algorithm, array):
    result = algorithm(array)
    return result


if __name__ == '__main__':

    # creating 100 element arrays sorted and not sorted
    array_sorted = list(range(1, 101))
    array_not_sorted = sorted(array_sorted, key=lambda x: random.random())

    # sort algorithms
    test_sort(sort.selection_sort, array_not_sorted)
    test_sort(sort.bubble_sort, array_not_sorted)
    test_sort(sort.merge_sort, array_not_sorted)

    # randomly picking element
    element = random.randint(1, 100)

    # search algorithms
    test_search(search.linear_search, element, array_not_sorted)
    test_search(search.binary_search, element, array_sorted)
    test_search(search.jump_search, element, array_sorted)
