


def sort(array):
    merge_sort(array, 0, len(array))


def insert_sort(array, start, length):
    i = start + 1
    while i < start + length:
        j = i
        while j > start:
            if array[j] >= array[j - 1]:
                break
            tmp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = tmp

            j -= 1

        i += 1


def merge_sort(array, start, length):
    if length <= 3:
        insert_sort(array, start, length)
        return

    mid = start + length / 2

    merge_sort(array, start, length / 2)
    merge_sort(array, mid, length - length / 2)

    i = start
    j = mid
    b = []
    while i < mid and j < start + length:
        if array[i] <= array[j]:
            b.append(array[i])
            i += 1
        else:
            b.append(array[j])
            j += 1

    while i < mid:
        b.append(array[i])
        i += 1
    while j < start + length:
        b.append(array[j])
        j += 1

    for k in range(length):
        array[start + k] = b[k]


if __name__ == "__main__":
    a = [2, 3, 5, 2, 7, 3, 4, 18, 8, 10, 12, 9]
    sort(a)
    #insert_sort(a, 0, len(a))
    print a
