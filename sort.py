"""-----------------------------------------------------------------

The library contains common algorithms and data structure examples.
Sort algorithms.

Title:          Most Common Algorithms
Author:         Roman Zajic
Last modified:  2022-12-11

-----------------------------------------------------------------"""


def selection_sort(array):
    n = len(array)

    for i in range(n):

        # find lowest
        low = i
        for j in range(i + 1, n):
            if array[j] < array[low]:
                low = j

        # swap first and lowest
        temp = array[low]
        array[low] = array[i]
        array[i] = temp

    print(array)
    return 0

def bubble_sort(array):

    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    print(array)
    return 0