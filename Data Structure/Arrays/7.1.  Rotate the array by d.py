# EX_1. 1 2 3 4 5 6 7
# d = 3
# 4 5 6 7 1 2 3

# EX_2. 1 2 3 4 5 6 7
# d = 2
# 3 4 5 6 7 1 2

# NOTE : MOVING FIRST D ELEMENTS TO END


# Naive Approach__
# 1. take a tempArr and copy first d elements to it
# 2 . while copying also shift arr[] elements to the elements which are copied
# 3. finally copy tempArray element to end of arr[]

def rotate(arr, d):
    tempArr = [0] * d

    for i in range(len(arr)):
        if (i < d):
            tempArr[i] = arr[i]
        if ((i + d) < len(arr)):
            arr[i] = arr[i + d]
    k = 0
    for j in range(len(arr) - d, len(arr)):
        arr[j] = tempArr[k]
        k = k + 1
    print(tempArr, arr)


# Better Approach
# 1.rotate the whole array by swapping the elements
# 2.now again rotate the first len-d element
# 3. now rotate the last d element


def reverse(arr, start, end):
    while (start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1


def rotateBetter(arr, d):
    n = len(arr)
    # edge cases:
    if (n == 0):
        return

    if d >= n and n != 0:
        d = d % n

    # 1. reverse the whole array:
    reverse(arr, 0, n - 1)
    print('revarr', arr)
    # 2. reverse the first len-d elements:
    reverse(arr, 0, n - d - 1)
    print('len_d', arr)
    # 3. reverse the last d elements:
    reverse(arr, n - d, n - 1)
    print('last_d', arr)


d = int(input())
arr = [int(i) for i in input().split()]
rotateBetter(arr, d)
print(arr)

# [5,6,7,1,2,3,4]