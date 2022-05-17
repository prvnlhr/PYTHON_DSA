import queue

import BinaryTreeInputPrint


def zigZigTraversal(root):
    if root is None:
        return None
    q = queue.Queue()
    q.put(root)
    level = 1
    zigzagTraversal = []

    while not q.empty():
        qsize = len(q.queue)
        levelNode = []

        for i in range(qsize):
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            levelNode.append(node.data)
        level += 1

        if level % 2 != 0:
            levelNode = levelNode[::-1]
        zigzagTraversal.append(levelNode)

    return zigzagTraversal


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = zigZigTraversal(root)
print(ans)
