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

def merge_sort(array):

    n = len(array)

    if n > 1:
        pivot = n // 2

        left = array[:pivot]
        right = array[pivot:]

        # sort left and right part
        merge_sort(left)
        merge_sort(right)

        # merge both parts
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
                k += 1
            else:
                array[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    print(array)
    return 0