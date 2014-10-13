

"""

Counting Sort Implementation

What is counting sort?

It is supposed that all the elements of an array are less than n and
each element is equal or greator than 0.

    2, 3, 1, 6, 5, 3, 0


      _1 _1 _1 _2 _  _1 _1 _  _  _  _

index  0  1  2  3  4  5  6  7  8  9


      _1 _2 _3 _5 _5 _6 _7 _  _  _  _

index  0  1  2  3  4  5  6  7  8  9

COMPLEXITY: O(n)

"""


def countsort(array, n):

    # initialize count array
    count_array = [0 for i in range(n + 1)]

    # count the number for each element
    for ele in array:
        count_array[ele] += 1

    # compute the positions
    i = 1
    while i <= n:
        count_array[i] += count_array[i - 1]
        i += 1

    new_array = [0 for x in range(len(array))]

    i = len(array) - 1
    while i >= 0:
        ele = array[i]

        # get the position of the element from count array
        pos = count_array[ele]
        new_array[pos - 1] = ele

        count_array[ele] -= 1
        i -= 1

    print new_array

if __name__ == "__main__":
    array = [2, 3, 1, 6, 5, 3, 0, 7, 9, 8, 7, 0, 3]
    countsort(array, 10)
