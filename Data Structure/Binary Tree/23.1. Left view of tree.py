import queue

import BinaryTreeInputPrint


# Input :
#                  1
#                /   \
#               2     3
#              / \     \
#             4   5     6
# Output : 1 2 4
#
# Input :
#         1
#       /   \
#     2       3
#       \
#         4
#           \
#             5
#              \
#                6
# Output :1 2 4 5 6


def leftViewHelper2(root):
    if root is None:
        return
    q = []
    q.append(root)
    result = []
    while len(q):
        n = len(q)
        for i in range(1, n + 1):
            ele = q[0]
            q.pop()
            if i == 1:
                result.append(ele.data)
            if ele.left is not None:
                q.append(ele.left)
            if ele.right is not None:
                q.append(ele.right)
    print(result)


# _ O(N)


# Preorder traversal


#     -------------1---------------  level 1    maxLevel = 0
#                /   \
#     ----------2------3-----------  level 2    maxLevel = 1
#             /   \     \
#    --------4-----5-----6---------  level 3    maxLevel = 2


result = []


def leftViewHelper(root, level, max_level):
    global result
    if root is None:
        return
    if max_level[0] < level:
        result.append(root.data)
        max_level[0] = level
    leftViewHelper(root.left, level + 1, max_level)
    leftViewHelper(root.right, level + 1, max_level)


def leftView(root):
    level = 1
    max_level = [0]
    leftViewHelper(root, level, max_level)
    return result


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = leftView(root)
print(ans)
# 2 2 13 7 10 1 10 5 2 -1 14 5 11 5 5 13 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 2 3 4 5 -1 7 -1 -1 6 -1 -1 -1 -1 -1
