"""-----------------------------------------------------------------

The library contains common algorithms and data structure examples.

Title:          Common Algorithms
Author:         Roman Zajic
Last modified:  2022-12-11

-----------------------------------------------------------------"""

import random
import search
import sort
import data_structures

def test_search(algorithm, element, array):
    result = algorithm(element, array)
    return result

def test_sort(algorithm, array, low = None, high = None):

    if high == low is None:
        algorithm(array)
    else:
        algorithm(array, low, high)

    print("Array sorted using", algorithm.__name__, ":")
    print(array)
    return 0


if __name__ == '__main__':

    """
    # creating 100 element arrays sorted and not sorted
    array_sorted = list(range(0, 100))
    array_not_sorted = sorted(array_sorted, key=lambda x: random.random())

    # sort algorithms
    test_sort(sort.selection_sort, array_not_sorted)
    test_sort(sort.bubble_sort, array_not_sorted)
    test_sort(sort.merge_sort, array_not_sorted)
    test_sort(sort.quick_sort, array_not_sorted, 0, 99)

    # randomly picking element
    element = random.randint(0, 99)

    # search algorithms
    test_search(search.linear_search, element, array_not_sorted)
    test_search(search.binary_search, element, array_sorted)
    test_search(search.jump_search, element, array_sorted)
    """

    linkedList = data_structures.LinkedList()
    linkedList.add_item(1)
    linkedList.add_item(2)
    linkedList.add_item(3)
    linkedList.remove_item(19)
    linkedList.remove_item(27)
    linkedList.remove_item(73)

    print(linkedList.search_item(1))

    print(linkedList)
