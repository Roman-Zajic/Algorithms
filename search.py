"""-----------------------------------------------------------------

The library contains common algorithms and data structure examples.
Search algorithms.

Title:          Most Common Algorithms
Author:         Roman Zajic
Last modified:  2022-12-11

-----------------------------------------------------------------"""

import math


def linear_search(element, array):
    n = len(array)
    i = 0

    while i < n:

        if array[i] == element:
            print(array[i], "found on position", i)
            return 0

        i += 1

    print(element, " not found")
    return 1


def binary_search(element, array):
    high = len(array) - 1
    low = 0

    while low < high:

        mid = (high + low) // 2
        if array[mid] >= element:
            high = mid
        else:
            low = mid + 1

    if array[low] == element:
        print(array[low], "found on position", low)
    else:
        print(element, "not found")


def jump_search(element, array):
    n = len(array)
    jump = int(math.sqrt(n))
    step = 0

    while step * jump < n and array[step * jump] < element:
        step += 1
    step = min(0, step - 1)

    # linear search
    i = step * jump
    while i < n:

        if array[i] == element:
            print(array[i], "found on position", i)
            return 0

        i += 1

    print(element, " not found")
    return 1