

def sort(array):
    quick_sort(array, 0, len(array) - 1)


def partition(array, left, right):
    pivot = array[(left + right) / 2]

    i = left
    j = right
    while i <= j:
        while array[i] < pivot:
            i += 1
        while j >= 0 and array[j] >= pivot:
            j -= 1

        if i < j:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

    return i


def quick_sort(array, left, right):
    index = partition(array, left, right)
    if left < index - 1:
        quick_sort(array, left, index - 1)
    if index + 1 < right:
        quick_sort(array, index, right)

if __name__ == "__main__":
    a = [2, 3, 5, 2, 7, 3, 4, 18, 8, 10, 12, 9]
    sort(a)
    #insert_sort(a, 0, len(a))
    print a
