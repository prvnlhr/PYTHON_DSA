#      Input:
#             30
#            /
#           20
#          /
#         10

#      Output:
#           20
#         /   \
#       10     30
#
#
#      Input:
#               4
#              /
#             3
#            /
#           2
#          /
#         1
#      Output:
#            3            3           2
#          /  \         /  \        /  \
#         1    4   OR  2    4  OR  1    3   OR ..
#          \          /                   \
#           2        1                     4
#
#      Input:
#                4
#              /   \
#             3     5
#            /       \
#           2         6
#          /           \
#         1             7
#      Output:
#             4
#          /    \
#         2      6
#       /  \    /  \
#      1    3  5    7


import BST


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def BSTtoBalancedBST(root):
    sortedInorder = []

    def getInorder(root):
        if root is None:
            return None
        getInorder(root.left)
        sortedInorder.append(root.data)
        getInorder(root.right)

    def buildBalancedBST(inorderArray):

        if len(inorderArray) <= 0:
            return None
        midIndex = len(inorderArray) // 2
        root_val = inorderArray[midIndex]
        root = Node(root_val)

        root.left = buildBalancedBST(inorderArray[0:midIndex])
        root.right = buildBalancedBST(inorderArray[midIndex + 1:])
        return root

    # 1. get sorted Inorder
    getInorder(root)

    # 2. Build balanced bst
    root = buildBalancedBST(sortedInorder)
    return root


bstRoot = BST.buildLevelTree()
root = BSTtoBalancedBST(bstRoot)
BST.PrintLevelWise(root)
