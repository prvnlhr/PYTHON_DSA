def findEle(mat, k):
    def binarySearch(rowIndex, lo, hi):
        midIndex = (lo + hi) // 2

        if mat[rowIndex][midIndex] == k:
            return rowIndex, midIndex

        elif mat[rowIndex][midIndex] < k:

            return binarySearch(rowIndex, midIndex + 1, hi)


        elif mat[rowIndex][midIndex] > k:
            return binarySearch(rowIndex, lo, midIndex - 1)

    rows = len(mat) - 1
    cols = len(mat[0]) - 1

    i = 0
    j = rows

    while i <= rows and j <= cols:
        midRowsIndex = (i + j) // 2

        leftMost = mat[midRowsIndex][0]
        rightMost = mat[midRowsIndex][cols]

        if leftMost == k:
            return midRowsIndex, 0
        elif rightMost == k:
            return midRowsIndex, cols

        elif leftMost < k and k < rightMost:
            return binarySearch(midRowsIndex, 0, cols)

        elif k < leftMost:
            j = j - 1
        elif rightMost < k:
            i = i + 1


def searchInSorted(mat, k):
    rows = len(mat) - 1
    cols = len(mat[0]) - 1

    def binarySearchInRow(midRowIndex, start, end):

        midIndex = (start + end) // 2
        midEle = mat[midRowIndex][midIndex]
        if k == midEle:
            return midRowIndex, midIndex
        elif k < midEle:
            return binarySearchInRow(midRowIndex, start, midIndex - 1)
        elif k > midEle:
            return binarySearchInRow(midRowIndex, midIndex + 1, end)

        # find the compatible row,to search the required ele.

    i = 0
    # j = cols
    j = rows

    while i <= rows and j <= cols:
        midRow = (i + j) // 2
        leftMost = mat[midRow][0]
        rightMost = mat[midRow][cols]

        if k == leftMost:
            return midRow, 0
        elif k == rightMost:
            return midRow, cols

        if leftMost < k and k < rightMost:
            return binarySearchInRow(midRow, 0, cols)
        elif k < leftMost:
            j = j - 1
        elif k > rightMost:
            i = i + 1


mat = [[0, 6, 8, 9, 11],
       [20, 22, 28, 29, 31],
       [36, 38, 50, 61, 63],
       [64, 66, 100, 122, 128]]

k = int(input())
# ans = searchInSorted(mat, k)
ans2 = findEle(mat, k)
print(ans2)
