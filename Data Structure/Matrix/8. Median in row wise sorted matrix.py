import sys


# HERE WE ARE COUNTING FOR EVERY ELEMENT
# IN CURR ROW WHICH ARE SMALLER THEN MID.
# NOW WE CAN USE LINER SEARCH ALL SEARCH
# TO COUNT, BUT TO OPTIMISE IT,
# WE CAN USE BINARY SEARCH AS THE CURR ROW IS SORTED
# currRow[mid_index] we decide if all smaller ele then MID
# will lie in left of right,
# SO we will only search half row.

def countElementsSmallerThenEqualToMid(MID, currRow):
    lo = 0
    hi = len(currRow) - 1

    while lo <= hi:
        midIndex = (lo + hi) // 2

        if currRow[midIndex] <= MID:
            lo = midIndex + 1
        else:
            hi = midIndex - 1
    return lo


def medianInSortedMat(mat):
    rows = len(mat)
    cols = len(mat[0])

    lo = sys.maxsize
    hi = -sys.maxsize
    # One intuition to find lo and hi would be to take topMost left element and bottomMost right ele
    # [[0, 6, 8, 9, 11],
    # [20, 22, 28, 29, 31],            lo = 0 , hi = 128 , all elements are in range 0 -> 128
    # [36, 38, 50, 61, 63],
    # [64, 66, 100, 122, 128]]

    # but what if matrix is like below,
    # [[5]
    #  [4]
    #  [3]
    #  [1]
    #  [3]                            lo = 5 , hi = 3
    #  [1]
    #  [4]
    #  [2]
    #  [5]
    #  [3]
    #  [3]]

    # SO we run loop to find lo and hi , rather then just taking topMost left and bottomMost right element

    for row in mat:
        lo = min(lo, row[0])
        hi = max(hi, row[cols - 1])

    while lo <= hi:
        mid = (lo + hi) // 2

        count = 0
        for currRow in mat:
            count += countElementsSmallerThenEqualToMid(mid, currRow)

        if count <= ((rows * cols) // 2):
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


mat = [[0, 6, 8, 9, 11], [20, 22, 28, 29, 31], [36, 38, 50, 61, 63], [64, 66, 100, 122, 128]]
# mat = [[1, 3, 4], [2, 5, 6], [7, 8, 9]]
ans = medianInSortedMat(mat)
print(ans)
