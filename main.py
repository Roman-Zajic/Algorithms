"""-----------------------------------------------------------------

The library contains common algorithms and data structure examples.

Title:          Most Common Algorithms
Author:         Roman Zajic
Last modified:  2022-12-11

-----------------------------------------------------------------"""

import random
import search


if __name__ == '__main__':

    # creating 100 element arrays sorted and not sorted
    array_sorted = list(range(1, 101))
    array_not_sorted = sorted(array_sorted, key=lambda x: random.random())

    # randomly picking element
    element = random.randint(1, 100)

    # linear search
    search.linear_search(element, array_not_sorted)

    # binary search
    search.binary_search(element, array_sorted)

    # jump search
    search.jump_search(element, array_sorted)

    print(array_sorted)
    print(array_not_sorted)

    # check all elements

    # for i in array_sorted:
    #    jump_search(i, array_sorted)
    #    binary_search(i, array_sorted)
