from collections import defaultdict
import BinaryTreeInputPrint


# SEE STRIVER'S YT VIDEO
# SEE LEETCODE SOLUTION
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def constructTree(preorder, inorder):
    def construct(left, right):

        # using nonlocal keyword to change variable in nested function
        #     or
        # we can also use preIndex[0] if not using nonlocal keyword

        nonlocal preIndex

        if left > right:
            return None

        rootVal = preorder[preIndex]  # or preorder[preIndex[0]]
        root = Node(rootVal)
        preIndex += 1  # or preIndex[0] += 1

        root.left = construct(left, map[rootVal] - 1)
        root.right = construct(map[rootVal] + 1, right)
        return root

    map = defaultdict(list)
    for index, val in enumerate(inorder):
        map[val] = index

    preIndex = 0  # or preIndex = [0]
    return construct(0, len(preorder) - 1)


def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.data, end=' ')
    Inorder(root.right)


BT = BinaryTreeInputPrint
# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 1, 2, 20, 15, 7]
inorder = [1, 9, 2, 3, 15, 20, 7]

root = constructTree(preorder, inorder)
# Inorder(root)
BT.PrintLevelWise(root)
