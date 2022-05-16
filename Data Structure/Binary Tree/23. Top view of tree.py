import queue
import sys
from collections import defaultdict

import BinaryTreeInputPrint


# Ex_1 :
#                1
#             /     \
#            2       3
#           /  \    / \
#          4    5  6   7
#
# Top view of the above binary tree is : 4 2 1 3 7
#
#  Ex_2 :    [ 2  1  3 6 ]
#              |  1  | |
#              |/ | \| |
#              2  |  3 |
#              |\ |  | |
#              |  4  | |
#              |  |\ | |
#              |  |  5 |
#              |  |  |\|
#              |  |  | 6

# Top view of the : 2 1 3 6


# STRIVER'S YT VIDEO
# LINE DIAGRAM APPROACH :

#                 0
#           -1    |    1
#       -2   |    |    |   2
#        |   |    1    |   |
#        |   | /     \ |   |
#        |   2         3   |
#        | /   \     /   \ |
#        4      5   6      7


def topOfTree(root):
    if root is None:
        return None

    map = defaultdict(list)
    q = queue.Queue()
    q.put([root, 0])
    minEle = sys.maxsize
    maxEle = -sys.maxsize

    while not q.empty():
        node, dist = q.get()

        if dist not in map:
            map[dist] = node.data
            minEle = min(minEle, dist)
            maxEle = max(maxEle, dist)

        if node.left:
            q.put([node.left, dist - 1])
        if node.right:
            q.put([node.right, dist + 1])

    for value in range(minEle, maxEle + 1):
        print(map[value])


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = topOfTree(root)
