# EX__. [ [ 1 , 3 , 5 , 7 ] , [2 , 4 , 6 , 8 ] , [ 0 , 9 , 10 , 11] ]
# Here rows == 3 ,cols == 4
# rows = k = 3
# cols = 4
# matrix = {
# 1 3 5 7
# 2 4 6 8
# 0 9 10 11 }
# O/P => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

from heapq import *


def mergeKSortedArrays(arrays, k):
    minHeap = []

    # IDEA::__
    # 1. Initially push first element of every row in minHeap along with its i and j position
    # 2. Now while minHeap,
    #    Pop the element from minHeap, which will be minimum element and append it to result
    # 3. if next element exist of that popped element in that row of matrix push it to minHeap
    # 4. Repeat above steps

    for i, arr in enumerate(arrays):
        # NOTE:: (arr[0], i, 0)
        #             |   |  |
        #             |   |  0 because j will be zero for every first element in row
        #             |   |
        #             |   i will be i
        #             |
        #             first element will be at arr[0]
        #
        heappush(minHeap, (arr[0], i, 0))

    heapify(minHeap)
    resultSortedArray = []
    while minHeap:
        num, i, j = heappop(minHeap)
        resultSortedArray.append(num)
        if j + 1 < len(arrays[i]):
            heappush(minHeap, (arrays[i][j + 1], i, j + 1))

    return resultSortedArray


rows = int(input())
col = int(input())
mat = [[int(i) for i in input().strip().split()] for i in range(rows)]

sortedArray = mergeKSortedArrays(mat, rows)
print(sortedArray)
