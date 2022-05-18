import collections
import queue
import sys

import BinaryTreeInputPrint


# Ex_1
#                       20
#                     /    \
#                   8       22
#                 /   \      \
#               5      3      25
#                     / \
#                   10   14
#  5, 10, 3, 14, 25

# Ex_2
#
#                       20
#                     /    \
#                   8       22
#                 /   \    /   \
#               5      3 4     25          3 4 are overlapping so always give right most ele
#                      / \
#                    10    14
#     5, 10, 4, 14, 25

def bottomView(root):
    if root is None:
        return

    map = collections.defaultdict(list)
    q = queue.Queue()
    q.put([root, 0])
    minDist = sys.maxsize
    maxDist = -sys.maxsize


    while not q.empty():
        node, dist = q.get()

        if dist not in map:
            map[dist] = node.data
            minDist = min(minDist, dist)
            maxDist = max(maxDist, dist)

        elif dist in map:
            map[dist] = node.data
            minDist = min(minDist, dist)
            maxDist = max(maxDist, dist)

        if node.left:
            q.put([node.left, dist - 1])
        if node.right:
            q.put([node.right, dist + 1])

    for value in range(minDist, maxDist + 1):
        print(map[value], end=' ')


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = bottomView(root)
# 20 8 22 5 3 -1 25 -1 -1 10 14 -1 -1 -1 -1 -1 -1
