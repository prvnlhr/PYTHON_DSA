# height = [6, 2, 5, 4, 5, 1, 6]
# maxArea = 12
# For every bar ‘x’, we calculate the area with ‘x’ as the
# smallest bar in the rectangle.If we calculate such area
# for every bar ‘x’ and find the maximum of all areas, our task is done.
#  How to calculate area with ‘x’ as smallest bar? We need to know index
# of the first smaller (smaller than ‘x’) bar on left of ‘x’ and index
# of first smaller bar on right of ‘x’. Let us call these indexes as
# ‘left index’ and ‘right index’ respectively. We traverse all bars
# from left to right, maintain a stack of bars. Every bar is pushed
# to stack once. A bar is popped from stack when a bar of smaller
# height is seen. When a bar is popped, we calculate the area with
# the popped bar as smallest bar. How do we get left and right indexes
# of the popped bar – the current index tells us the ‘right index’ and
# index of previous item in stack is the ‘left index’. Following is the
# complete algorithm.
#
# __BRUTE FORCE SOLUTION______________
# CALCULATE NSL AND NSR for every height O(N^2) ___________________
#
# ______ OPTIMISED SOLUTION___________ STRIVER'S video
#
# T: O(N) ,S:(N)+(N)+(N) THREE PASS ,STACK BASED ,
# EASY IMPLEMENTATION AND UNDERSTANDABLE__________
#
def maxAreaOfHist(heights):
    n = len(heights)
    stack = []
    leftSmallest, rightSmallest = [0] * n, [0] * n

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            leftSmallest[i] = stack[-1] + 1  # we are doing +1,
            # because we are considering limit till we get NSL
        else:
            # if stack has no height greater in left, then limit will be
            # length arr last limit left side, i.e 0
            leftSmallest[i] = 0
        stack.append(i)
    print(leftSmallest)
    print(rightSmallest)
    print(heights)
    # clear stack
    while stack:
        stack.pop()

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

    maxArea = 0
    for index in range(n):
        print(heights[index])
        maxArea = max(maxArea, heights[index] * (rightSmallest[index] - leftSmallest[index] + 1))
        print(maxArea)
        print()
    return maxArea


# Stack based O(N),O(N), single pass
# STRIVER's SOLUTION
# # BEST SOLUTION BUT TRICKY

def maxAreaOfHist1(heights):
    stack = []
    maxArea = 0
    n = len(heights)
    for i in range(n):
        while stack and (i == n or heights[stack[-1]] >= heights[i]):
            height = heights[stack[-1]]
            stack.pop()
            width = i if len(stack) == 0 else i - stack[-1] - 1
            maxArea = max(maxArea, width * height)
        stack.append(i)
    return maxArea


# _GFG STACK SOLUTION_______
def maxAreaOfHist2(hist):
    stack = []
    currIndex = 0
    max_Area = 0
    while currIndex < len(hist):
        # if not stack
        if (not stack) or hist[currIndex] >= hist[stack[-1]]:
            stack.append(currIndex)
            currIndex = currIndex + 1
        # if stack
        else:
            stackTop = stack.pop()
            if stack:
                area = hist[stackTop] * (currIndex - stack[-1] - 1)
            else:
                area = hist[stackTop] * currIndex

            max_Area = max(max_Area, area)  # update maxArea
    # ______________________________
    while stack:
        stackTop = stack.pop()
        if stack:
            area = hist[stackTop] * (currIndex - stack[-1] - 1)
        else:
            area = hist[stackTop] * currIndex
        max_Area = max(max_Area, area)
    return max_Area


# hist = [int(i) for i in input().strip().split()]
# hist = [6, 2, 5, 4, 5, 1, 6]
hist =[2,1,5,6,2,3]

# hist = [4, 2, 1, 5, 6, 3, 2, 4, 2]
# hist = [3, 0, 2, 0, 4]
print(maxAreaOfHist(hist))
