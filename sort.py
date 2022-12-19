"""-----------------------------------------------------------------

The library contains common algorithms and data structure examples.
Sort algorithms.

Title:          Common Algorithms
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
        array[low], array[i] = array[i], array[low]

    return 0


def bubble_sort(array):

    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # swap if next element is lower
                array[j], array[j + 1] = array[j + 1], array[j]

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

    return 0


def partition(array, low, high):

    i = low
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            # swap if the element is lower then pivot
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[high] = array[high], array[i]

    return i


def quick_sort(array, low, high):

    if low < high:

        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)

    return 0
