import heapq


# T: klogk

def printInSortedOrder(mat, k):
    res = []
    rows = len(mat)
    cols = len(mat[0])
    min_heap = []
    for i in range(rows):
        min_heap.append((mat[i][0], i, 0))
    heapq.heapify(min_heap)
    count = 0
    while min_heap:
        ele, i, j = heapq.heappop(min_heap)
        count = count + 1
        if count == k:
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
k = 7
printInSortedOrder(mat, k)
