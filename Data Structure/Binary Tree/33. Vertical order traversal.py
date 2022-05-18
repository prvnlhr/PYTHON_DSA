import queue
import sys
from collections import defaultdict

import BinaryTreeInputPrint


#
#
#                1
#             /     \
#            2       3
#          /   \   /   \
#         4     5 6     7
#                     /   \
#                    8     9


#         |  |   |   |  |  |
#         |  |   1   |  |  |
#         |  |/  |  \|  |  |
#         |  2   |   3  |  |
#         |/ | \ | / | \|  |
#         4  |  5 6  |  7  |
#         |  |   |   |/ | \|
#         |  |   |   8  |  9

# The output of print this tree vertically will be:
# 4
# 2
# 1 5 6
# 3 8
# 7
# 9

# APPROACH :
# STRIVER'S YT VIDEO
# LINE DIAGRAM APPROACH
def verticalOrderTraversal(root):
    if root is None:
        return None

    map = defaultdict(list)
    q = queue.Queue()
    q.put([root, 0])
    minVerticalDist = sys.maxsize
    maxVerticalDist = -sys.maxsize

    while not q.empty():
        node, dist = q.get()

        if dist not in map:
            map[dist] = [node.data]
            minVerticalDist = min(minVerticalDist, dist)
            maxVerticalDist = max(maxVerticalDist, dist)

        elif dist in map:
            map[dist].append(node.data)
            minVerticalDist = min(minVerticalDist, dist)
            maxVerticalDist = max(maxVerticalDist, dist)

        if node.left:
            q.put([node.left, dist - 1])
        if node.right:
            q.put([node.right, dist + 1])

    for value in range(minVerticalDist, maxVerticalDist + 1):
        print(map[value])


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = verticalOrderTraversal(root)
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 8 -1 9 -1 -1 -1 -1
