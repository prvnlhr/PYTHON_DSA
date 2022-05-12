import BinaryTreeInputPrint


def findPath(root, n, path):
    if root is None:
        return False
    path.append(root.data)

    if root.data == n:
        return True

    if (root.left and findPath(root.left, n, path)) or (root.right and findPath(root.right, n, path)):
        return True

    path.pop()
    return False


def LCA(root, n1, n2):
    path1 = []
    path2 = []
    findPath(root, n1, path1)
    findPath(root, n2, path2)
    print(path1)
    print(path2)
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i = i + 1
    return path1[i - 1]


# STEPS :__
# 1._recur left subtree and find lca
# 2._recur right subtree and find lca
# 3._if we get left_lca and right_lca, then root is lca
# 4._else return which is not None from left and right lca
#
# O(N) solution
def LCAOptimize(root, n1, n2):
    if root is None:
        return None

    # if root is equal to n1 or n2,then return root
    if root.data == n1 or root.data == n2:
        return root

    left_lca = LCAOptimize(root.left, n1, n2)
    right_lca = LCAOptimize(root.right, n1, n2)

    # if we find left_lca and right_lca in left and right
    # subtree ,that means root is lca
    if left_lca and right_lca:
        return root
    # else return a lca which is not None
    return left_lca if left_lca is not None else right_lca


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
# 8,15  -> 5
# 11,15 -> 9

BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
n1 = int(input())
n2 = int(input())
ans = LCA(root, n1, n2)
print(ans)
