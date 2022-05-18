import copy
from collections import defaultdict

import BinaryTreeInputPrint


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 1 2 3 4 5 6 7 -1 -1 8 9 -1 -1 -1 -1 12 -1 11 14 -1 18 -1 -1 15 20 -1 -1 17 16 -1 -1 -1 -1 -1 -1
#
#                1
#            /      \
#           2        3
#         /   \     /   \
#        4     5   6     7
#            /   \
#           8     9
#          /     /   \
#         12     11    14
#          \          / \
#           18       15   20
#                    / \
#                   17    16


def distance(root, x, y):
    def nodeDist(root, node, dist):

        if root is None:
            return 0
        if root.data == node:
            return dist

        return nodeDist(root.left, node, dist + 1) or nodeDist(root.right, node, dist + 1)

    def LCA(root, x, y):

        if root is None:
            return None

        if root.data == x or root.data == y:
            return root.data

        left_lca = LCA(root.left, x, y)
        right_lca = LCA(root.right, x, y)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca else right_lca

    lca = LCA(root, x, y)
    dist1 = nodeDist(lca, x, 0)
    dist2 = nodeDist(lca, y, 0)
    print(dist1 + dist2 + 1)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
print(distance(root, 18, 16))
