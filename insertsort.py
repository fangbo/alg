

def insert(array, start, end):

    j = start

    while j <= end:
        i = j

        print "i=%s, j=%s" % (i, j)
        a = array[i]
        while i > start:
            if a >= array[i - 1]:
                break

            array[i] = array[i - 1]
            i -= 1

        array[i] = a

        j += 1


def insert_sort(array):
    insert(array, 0, len(array) - 1)


if __name__ == "__main__":

    array = [100 - i for i in range(100)]

    insert_sort(array)

    print array

    from sorttest import test
    test(insert_sort)
