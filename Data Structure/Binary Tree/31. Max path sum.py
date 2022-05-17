import queue
import sys

import BinaryTreeInputPrint

# STRIVER'S YT VIDEO
# Ex_
#                  10
#                /    \
#               2      10
#             /   \       \
#           20     1      -25
#                         /  \
#                        3    4
#
# maxPathValue = 42 => 20 -> 2 -> 10 -> 10

# 1 2 3 4 5 6 7 -1 -1 8 9 -1 -1 -1 -1 -1 -1 -1 -1

maxPathValue = [-sys.maxsize]
class Solution:

    def maxPathSumHelper(self,root):
        global maxPathValue
        if root is None:
            return 0

        # find left and right path
        left = self.maxPathSumHelper(root.left)
        right = self.maxPathSumHelper(root.right)

        # if left is -ve or right is -ve then leftMaxPath would be zero or rightPath would be zero
        leftMaxPath = max(0, left)
        rightMaxPath = max(0, right)

        # maxPathValue would be maximum of left and right max including root.data
        maxPathValue[0] = max(maxPathValue[0], leftMaxPath + rightMaxPath + root.data)
        return max(leftMaxPath, rightMaxPath) + root.data

    def maxPathSum(self, root):
        global maxPathValue
        self.maxPathSumHelper(root)
        return maxPathValue[0]


# maxPathValue = [-sys.maxsize]
#
#
# def maxPathSumHelper(root):
#     global maxPathValue
#     if root is None:
#         return 0
#
#     # find left and right path
#     left = maxPathSumHelper(root.left)
#     right = maxPathSumHelper(root.right)
#
#     # if left is -ve or right is -ve then leftMaxPath would be zero or rightPath would be zero
#     leftMaxPath = max(0, left)
#     rightMaxPath = max(0, right)
#
#     # maxPathValue would be maximum of left and right max including root.data
#     maxPathValue[0] = max(maxPathValue[0], leftMaxPath + rightMaxPath + root.data)
#     return max(leftMaxPath, rightMaxPath) + root.data
#
#
# def maxPathSum(root):
#     maxPathSumHelper(root)
#     return maxPathValue[0]


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
obj = Solution()
ans = obj.maxPathSum(root)
# ans = maxPathSum(root)
print(ans)
