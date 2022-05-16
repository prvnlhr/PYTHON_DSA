# This function returns pointer to LCA of
# two given values n1 and n2.
import sys

import BinaryTreeInputPrint


# Find the distance between two keys in a binary tree, no
# parent pointers are given. The distance between two nodes
# is the minimum number of edges to be traversed to reach
# one node from another.

def isNodePresent(root, node):
    # base case
    if root is None:
        return False

    # if the node is found, return true
    if root == node:
        return True

    # return true if the node is found in the left or right subtree
    return isNodePresent(root.left, node) or isNodePresent(root.right, node)


# Function to find the level of a given node present in a binary tree
def findLevel(root, node, level):
    # base case
    if root is None:
        return -sys.maxsize
    if root.data == node:
        return level
    left = findLevel(root.left, node, level + 1)
    if left != -sys.maxsize:
        return left
    return findLevel(root.right, node, level + 1)


# def findLevel(root, k, level):
#     if root is None:
#         return -1
#     if root.data == k:
#         return level
#     l = findLevel(root.left, k, level + 1)
#     if l != -1:
#         return l
#     return findLevel(root.right, k, level + 1)
#
#

# Function to find the lowest common ancestor of given nodes `x` and `y`,
# where both `x` and `y` are present in a binary tree.
def findLCA(root, x, y):
    # base case 1: if the tree is empty
    if root is None:
        return None

    # base case 2: if either `x` or `y` is found
    if root.data == x or root.data == y:
        return root

    # recursively check if `x` or `y` exists in the left subtree
    left = findLCA(root.left, x, y)

    # recursively check if `x` or `y` exists in the right subtree
    right = findLCA(root.right, x, y)

    # if `x` is found in one subtree and `y` is found in the other subtree,
    # update lca to the current node
    if left and right:
        return root

    # if `x` and `y` exist in the left subtree
    if left:
        return left

    # if `x` and `y` exist in the right subtree
    if right:
        return right

    return None


# Function to find the distance between node `x` and node `y` in a
# given binary tree rooted at `root` node
def findDistance(root, x, y):
    print(root.data, x, y)
    # `lca` stores the lowest common ancestor of `x` and `y`
    lca = None

    # call LCA procedure only if both `x` and `y` are present in the tree
    # if isNodePresent(root, y) and isNodePresent(root, x):
    lca = findLCA(root, x, y)

    # else:
    #     return -sys.maxsize
    print(lca.data)
    # return distance of `x` from lca + distance of `y` from lca
    return findLevel(lca, x, 0) + findLevel(lca, y, 0)


#
# def lca(root, n1, n2):
#     # Base case
#     if root is None:
#         return root
#
#     if root.data == n1 or root.data == n2:
#         return root
#     left = lca(root.left, n1, n2)
#     right = lca(root.right, n1, n2)
#
#     if left and right:
#         return root
#     if left:
#         return left
#     else:
#         return right
#
#
# def findLevel(root, k, level):
#     if root is None:
#         return -1
#     if root.data == k:
#         return level
#
#     l = findLevel(root.left, k, level + 1)
#     if l != -1:
#         return level
#     return findLevel(root.right, k, level + 1)
#
#
# def find_distance_between_two_nodes(root, n1, n2):
#     least_common_ancestor = lca(root, n1, n2)
#     print(least_common_ancestor.data)
#     if least_common_ancestor:
#         d1 = findLevel(least_common_ancestor, n1, 0)
#         d2 = findLevel(least_common_ancestor, n2, 0)
#         print(d1, d2)
#         return d1 + d2
# __________________________________________________________
# Self solved 100% gfg passed

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
# 1 2 3 -1 4 5 6 -1 -1 7 8 -1 -1 -1 -1 -1 -1
# 7
# 6
n1 = int(input())
n2 = int(input())
ans = findDistance(root, n1, n2)
print(ans)
