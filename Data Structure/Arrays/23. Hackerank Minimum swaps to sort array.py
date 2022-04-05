import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = -1
    map = {}
    for i in range(len(arr)):
        map[arr[i]] = i
    # print(map)
    sorted = [i for i in range(1, len(arr) + 1)]
    # print(sorted)
    for i in range(len(arr)):
        if (arr[i] != sorted[i]):
            swaps = swaps + 1
            init = arr[i]
            a = map.get(sorted[i])
            i, a = a, i
            map[init] = map[sorted[i]]
            map[sorted[i]] = i
    # print(arr)
    return swaps


def minimumSwaps(arr):
    # initialize number of swaps as 0
    swaps = 0
    # create a dictionary which holds value, index pairs of our array
    # [4,3,1,2] --> {4: 1, 3: 2, 1: 3, 2: 4}
    getIndex = dict(zip(arr, range(1, len(arr) + 1)))
    for i in range(1, len(arr) + 1):
        # swap only if value is not equal to index
        if getIndex[i] != i:
            """
            Example of a proper swap when i=1
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 1, 2: 4}
            [4,3,1,2] --> [1,3,4,2]
            Full swap is not required i.e. we don't have to set 1:1 or arr[0]=1(i:i or arr[i-1]=i) because we will never use these two values again. Therefore we can keep these two values as it is. And thus our swap looks as follows.
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 3, 2: 4}
            [4,3,1,2] --> [4,3,4,2]
            """
            getIndex[arr[i - 1]] = getIndex[i]
            arr[getIndex[i] - 1] = arr[i - 1]
            swaps += 1
    return swaps


n = int(input())
arr = list(map(int, input().split()))
print(minimumSwaps(arr))

if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]

    res = minimumSwaps(arr)
    print(res)
