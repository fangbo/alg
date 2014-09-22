
"""
The quick sort implementation from the Introduction to Algorithm
"""


def partition(array, start, end):
    pivot = array[start]

    j = start + 1
    i = start

    while j <= end:
        if array[j] <= pivot:
            i += 1
            a = array[i]
            array[i] = array[j]
            array[j] = a

        j += 1

    array[start] = array[i]
    array[i] = pivot

    return i


def quicksort(array, start, end):
    partindex = partition(array, start, end)

    if start < partindex:
        quicksort(array, start, partindex - 1)

    if partindex < end:
        quicksort(array, partindex + 1, end)


if __name__ == "__main__":
    array = [100 - i for i in range(100)]

    print array

    quicksort(array, 0, len(array) - 1)

    print array
