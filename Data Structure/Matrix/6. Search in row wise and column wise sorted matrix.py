def searchEle(mat, k):
    rows = len(mat)
    cols = len(mat[0])
    i = 0
    j = cols - 1

    while i < rows and j >= 0:

        if mat[i][j] == k:
            return i, j

        elif mat[i][j] < k:
            i = i + 1

        elif mat[i][j] > k:
            j = j - 1


# Approach: The simple idea is to remove a row or column in
# each comparison until an element is found. Start searching
# from the top-right corner of the matrix. There are three possible cases.
# The given number is greater than the current number: This will
# ensure that all the elements in the current row are smaller
# than the given number as the pointer is already at the right-most
# elements and the row is sorted. Thus, the entire row gets
# eliminated and continues the search for the next row. Here,
# elimination means that a row needs not be searched.
# The given number is smaller than the current number: This
# will ensure that all the elements in the current column
# are greater than the given number. Thus, the entire column
# gets eliminated and continues the search for the previous
# column, i.e. the column on the immediate left.
# The given number is equal to the current number: This will end the search.

# Time Complexity: O(n).
# Only one traversal is needed, i.e, i from 0 to n and j from n-1 to 0
# with at most 2*n steps.
# The above approach will also work for m x n matrix (not only for n x n).
# Complexity would be O(m + n).
# Space Complexity: O(1).

def searchInSorted(mat, k):
    rows = len(mat)
    cols = len(mat[0])
    i = 0
    j = cols - 1

    while i < rows and j >= 0:
        currEle = mat[i][j]
        if currEle == k:
            return i, j
        elif currEle < k:
            i = i + 1
        elif currEle > k:
            j = j - 1


mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]
k = int(input())
ans1 = searchInSorted(mat, k)
ans2 = searchEle(mat, k)
print(ans1, ans2)
