import copy

import BinaryTreeInputPrint


#
#                1
#             /    \
#           2       3
#         /   \    /   \
#        4     5  6     7
#            /   \
#           8     9
#          /     /   \
#         6     11    14
#          \          / \
#           8       15   20
#                   / \
#                  7    6
#
#  node = 15
# 1 2 5 9 14 15
def pathToNodeP(root, node):
    res = []

    def find(root, node, path):
        if root is None:
            return []
        path.append(root.data)
        if root.data == node:
            res.append(copy.deepcopy(path))
        find(root.left, node, path)
        find(root.right, node, path)
        path.pop()

    find(root, node, [])
    return res


def pathToNode(root, node):
    res = []

    def findPath(root, node, path):
        if root is None:
            return False
        path = path + str(root.data)
        if root.data == node:
            res.append(path)
            return True
        path = path + ' '
        findPath(root.left, node, path) or findPath(root.right, node, path)

    findPath(root, node, '')
    return res


# # MY solution worked correctly
# def pathToN(root, node):
#     if root is None:
#         return False
#     if root.data == node:
#         path = []
#         path.append(root.data)
#         return path
#     pathLeft = pathToN(root.left, node)
#     if pathLeft:
#         pathLeft.insert(0, root.data)
#         return pathLeft
#     rightPath = pathToN(root.right, node)
#     if rightPath:
#         rightPath.insert(0, root.data)
#         return rightPath
#
#
# def findPath(root, pathArr, node):
#     if root is None:
#         return False
#
#     pathArr.append(root.data)
#     if root.data == node:
#         return True
#     if findPath(root.left, pathArr, node) or findPath(root.right, pathArr, node):
#         return True
#     pathArr.pop()
#     return False
#
#
# def pathToNode(root, node):
#     pathArray = []
#     if (findPath(root, pathArray, node)):
#         print(pathArray)

# 1 2 3 4 5 -1 8 17 -1 6 7 -1 9 -1 -1 -1 -1 10 12 -1 -1 -1 -1 14 -1 -1 -1
# 1 2 3 4 5 6 7 -1 -1 8 9 -1 -1 -1 -1 6 -1 11 14 -1 8 -1 -1 15 20 -1 -1 7 6 -1 -1 -1 -1 -1 -1
BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
node = int(input())
# n2 = int(input())
# pathToNode(root, node)
# ans = pathToN(root, node)
ans = pathToNodeP(root, node)
print(ans)
