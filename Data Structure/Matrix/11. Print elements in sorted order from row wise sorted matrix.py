import heapq


# Time complexity of this solution is O(N2LogN).
# APPROACH:: Using min_heap

# 1. Push all first element of every row in heap, because first element
#    of sorted order output will be minimum, and it will be minimum from all rows first ele.

# 2. while min_heap does not become empty, pop element and its  i,j from heap,which
#    will give smallest ele.

# 3. put this element into res, and check if next element exist, if yes then put it into heap.

def printInSortedOrder(mat):
    res = []
    rows = len(mat)
    cols = len(mat[0])
    min_heap = []

    for i in range(rows):
        min_heap.append((mat[i][0], i, 0))

    heapq.heapify(min_heap)

    while min_heap:
        ele, i, j = heapq.heappop(min_heap)
        res.append(ele)

        # if next of curr ele exists,
        if j + 1 < cols:
            heapq.heappush(min_heap, (mat[i][j + 1], i, j + 1))

    print(res)


# mat = [[1, 3, 4], [2, 5, 6], [7, 8, 9]]
mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50],
       ]
printInSortedOrder(mat)
