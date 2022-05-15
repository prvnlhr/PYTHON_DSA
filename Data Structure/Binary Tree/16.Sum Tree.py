import BinaryTreeInputPrint


# Given a Binary Tree where each node has positive and negative values.
# Convert this to a tree where each node contains the sum of the left
# right sub trees in the original tree. The values of leaf nodes
# are changed to 0.
#
# Ex_

#                   10
#                /      \
#              -2        6
#             /  \      /  \
#            8   -4    7    5


#                   20 (4-2 + 12 + 6)
#                /      \
#              4 (8-4)   12 (7+5)
#            /   \      /   \
#           0     0    0     0

def sumTree(root):
    if root is None:
        return 0
    oldValue = root.data
    leftSum = sumTree(root.left)
    rightSUm = sumTree(root.right)
    root.data = leftSum + rightSUm
    return root.data + oldValue


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
sumTree(root)
BT.PrintLevelWise(root)
