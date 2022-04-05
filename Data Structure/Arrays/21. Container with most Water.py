import sys


# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two
# endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
# LEETCODE 11
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by
# array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
# water (blue section) the container can contain is 49.

# Well the intuition is to find the max Area enclosed
# by two heights
# we can find area by base * height
# now the catch is if we have to find area enclosed by two height,
# let say height at index 4 is 7 and height at index 6 is 8
# so i == 4 (7) , i == 6 (8) , so base will be index 6 - 4 == 2
# now what is height enclosed by there two height ???
# if water has to be filled, between heights 7 and 8 , up to what max height water can be filled,
# we can fill it up to height 7 only , so from 7 and 8 we will use 7 as it is min
# therefore , area == base * min(height) -> 2 * 7 = 14
# we will use these idea to solve below problem taking height from i = 0 and j == len -1
#
def maxArea(height):
    l = len(height)
    i = 0
    j = l - 1
    area = 0

    while i < j:

        base = j - i
        height_till_water_can_be_contained = min(height[i], height[j])
        currArea = base * height_till_water_can_be_contained

        area = max(area, currArea)

        if (height[i] < height[j]):  # height at i is smaller
            i = i + 1
        elif (height[i] >= height[j]):  # height at j is smaller
            # smaller or both are equal
            j = j - 1
    return area


# def maxArea(A):
#     l = 0
#     r = len(A) - 1
#     area = 0
#
#     while l < r:
#         # Calculating the max area
#         area = max(area, min(A[l],
#                              A[r]) * (r - l))
#
#         if A[l] < A[r]:
#             l += 1
#         else:
#             r -= 1
#     return area


# height = [int(i) for i in input().split()]
testCases = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 5, 4, 3], [3, 1, 2, 4, 5]]
for test in testCases:
    height = test
    print(maxArea(height))
