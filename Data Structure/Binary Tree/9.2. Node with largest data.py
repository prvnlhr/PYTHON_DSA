import sys

import BinaryTreeInputPrint

# For a given Binary Tree of integers, find and return the sum of all the nodes data.
# Sample Input 1:
# 2 3 4 6 -1 -1 -1 -1 -1
# Sample Output 1:
#  15
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Sample Output 2:
#  28


largest = -sys.maxsize


def largestNode(root):
    global largest
    if root is None:
        return
    if root.data > largest:
        largest = root.data

    largestNode(root.left)
    largestNode(root.right)
    return largest


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = largestNode(root)
print(ans)
