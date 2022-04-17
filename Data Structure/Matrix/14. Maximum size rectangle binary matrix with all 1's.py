def maxAreaOfHist(heights):
    n = len(heights)
    stack = []
    leftSmallest, rightSmallest = [0] * n, [0] * n

    # NSL__
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            leftSmallest[i] = stack[-1] + 1  # we are doing +1 ,because we are considering limit till we get NSL
        else:
            # if stack has no height greater in left, then limit will be
            # length arr last limit left side ,i.e 0
            leftSmallest[i] = 0
        stack.append(i)
    # clear stack
    while stack:
        stack.pop()

    # NSR__
    for j in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[j]:
            stack.pop()
        if stack:
            rightSmallest[j] = stack[-1] - 1  # we are doing -1, because we are considering limit till we get NSR
        else:
            # if stack has no height greater in right, then limit will be
            # length arr last limit on right side ,i.e len -1
            rightSmallest[j] = n - 1
        stack.append(j)
    # finding maxArea from NSL and NSR
    # maxArea = (NSR-NSL + 1)*height
    maxArea = 0
    for index in range(n):
        maxArea = max(maxArea, heights[index] * (rightSmallest[index] - leftSmallest[index] + 1))
    return maxArea


# REFER ANUJ"S YOUTUBE VIDEO.

# APPROACH , THIS PROBLEM USES CONCEPT OF LARGEST AREA HISTOGRAM
# 1. Take first row of matrix and find maxAreaHist
# 2. for every other next row, first update the elements of currRow,
#     and then find the maxAreaHist, do it for very row
# 3. Update maxArea, obtained from currRow


#         0  1  1  0
#         1  1  1  1
#         1  1  1  1
#         1  1  0  0
# Take first row as base ->      0   1   1   0

# Find maxAreaHIst ->          ______|___|_____    buildings maxArea = 1 * 2 => 2

# Now take second row as ->      1   1   1   1
# base
#                                    |   |
#                             ___|___|___|___|______ maxArea = 2 * 2 => 4
#                       we have combine heights of row 1 and 2 , where value was 1
#
#
# Now take row 3 as ->
# base                               |   |
# #                              |   |   |   |
# #                           ___|___|___|___|______ maxArea = 2 * 4 => 8
# #                     we have combine heights of row 1 and 2 , where value was 1
# #
# Similarly for all row

# Complexity Analysis__:
# Time Complexity: O(R x C).
# Only one traversal of the matrix is required, so the time complexity is O(R X C)
# Space Complexity: O(C).
# Stack is required to store the columns, so  space complexity is O(C)

def findMaxRectangle(mat):
    currRow = mat[0]
    maxArea = maxAreaOfHist(currRow)
    rows = len(mat)
    cols = len(mat[0])
    for i in range(1, rows):
        for j in range(cols):
            if mat[i][j] == 1:
                currRow[j] += 1
            else:
                currRow[j] = 0
        currAns = maxAreaOfHist(currRow)
        maxArea = max(maxArea, currAns)
    return maxArea


testCases = [[[0, 1, 1, 0],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 0, 0]], [[0, 1, 1],
                              [1, 1, 1],
                              [0, 1, 1]]]
for mat in testCases:
    ans = findMaxRectangle(mat)

    print(ans)
