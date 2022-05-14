import copy

import BinaryTreeInputPrint


#                    1
#                  /   \
#                 2     3
#                / \   / \
#               4   5 6   7
#                  /   \
#                 8     9
#
#  1 2 3 4 5 6 7 -1 -1 -1 -1 8 -1 -1 9 -1 -1 -1 -1
#  -> [1, 2, 4]
#  -> [1, 2, 5]
#  -> [1, 3, 6, 8]
#  -> [1, 3, 7, 9]


# returns path array with path as a string
def pathRootToLeaf(root):
    # Leetcode easy , printing path string stored in array of paths
    def findPath(root, path):
        if root is None:
            return []
        # 1. Make path adding current node
        path = path + str(root.data)
        # 2. check if leaf node reached return path created until now
        if root.left is None and root.right is None:
            return [path]
        # This step just adds space between path nodes --> '2<space>3 4 5 6'
        path = path + ' '
        #
        # 3. Else explore left and right subtree
        # Below both call will get path array and we gonna
        # add then to create a combine array of paths
        return findPath(root.left, path) + findPath(root.right, path)

    return findPath(root, '')


# if we want to return array of paths containing paths array
def pathRootToLeaf(root):
    res = []

    def findPath(root, path):
        if root is None:
            return []

        path.append(root.data)

        if root.left is None and root.right is None:
            res.append(copy.deepcopy(path))

        findPath(root.left, path)
        findPath(root.right, path)
        path.pop()

    findPath(root, [])
    return res


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
# ans = rootToLeafPath(root)
ans = pathRootToLeaf(root)
print(ans)
