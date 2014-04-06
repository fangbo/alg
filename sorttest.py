
import random


def test(sort_function):
    length = 100000
    array = [random.randint(0, 100000000) for i in range(length)]

    sort_function(array)

    i = 0
    while i + 1 < length:
        if array[i] > array[i + 1]:
            print "right sorted array!"
            print "%s, %s" % (array[i], array[i + 1])
        i += 1
