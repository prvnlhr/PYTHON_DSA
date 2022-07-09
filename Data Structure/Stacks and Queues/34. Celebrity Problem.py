# This Based on The Approach of Graph
# This Problem has many solution based on Graph, Two-pointer,Stack
# Stack Sol is O(N) and O(N)
# Two Pointer sol are of Two types: 1) O(n ^ 2    2) O(n) and O(1)
#
#
# Input:
# MATRIX = { {0, 0, 1, 0},
#            {0, 0, 1, 0},
#            {0, 0, 0, 0},
#            {0, 0, 1, 0} }
# Output:id = 2
# Explanation: The person with ID 2 does not
# know anyone but everyone knows him
#
# Input:
# MATRIX = { {0, 0, 1, 0},
#            {0, 0, 1, 0},
#            {0, 1, 0, 0},
#            {0, 0, 1, 0} }
# Output: No celebrity
# Explanation: There is no celebrity.


# T : O(n) and O(1)
def findCelebrity(n, mat):
    start = 0
    end = n - 1
    # this loop find a potential candidate which can be celebrity
    while start < end:
        if mat[start][end] == 1:
            start = start + 1
        else:
            end = end - 1

    candidate = start
    # this loop finally , check if candidate is celebrity or not
    # conforming step
    for i in range(n):
        if i != candidate and (mat[candidate][i] == 1 or mat[i][candidate] == 0):
            #       0  1  2  3
            # ---|-----------------
            # 0  |  0  0  1  0
            # 1  |  0  0  1  0
            # 2  |  0  0  0  0                 now here candidate is i = 2 ,which may be celebrity
            # 3  |  0  0  1  0                 as we found from first while loop
            #    |                             but to confirm it we will run a second for loop
            #                                  for i = 2 row ,and j = 2 col, vertical and horizontal
            #                                  cells except (i=2,j=2) ,because if 2 is celeb,then checking
            #                                  if 2 knows 2 will be absurd so,we put i != candidate
            return -1

    return candidate


n = int(input())
mat = [[int(j) for j in input().strip().split()] for i in range(n)]
print(findCelebrity(n, mat))
