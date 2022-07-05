# Is Based on The Approach of Graph
# This Problem has many solution based on Graph, Two-pointer,Stack
# Stack Sol is O(N) and O(N)
# Two Pointer sol are of Two types: 1) O(n^2) 2) O(n) and O(1)
#
#

# O(n) and O(1)
def findCelebrity(n, mat):
    start = 0
    end = n - 1

    while start < end:
        if mat[start][end] == 1:
            start = start + 1
        else:
            end = end - 1

    for i in range(n):
        if i != start and (mat[start][i] == 1 or mat[i][start] == 0):
            return -1
    return start


n = int(input())
mat = [[int(j) for j in input().strip().split()] for i in range(n)]
print(findCelebrity(n, mat))
