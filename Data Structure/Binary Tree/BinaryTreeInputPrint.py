import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildLevelTree():
    levelorder = [int(i) for i in input().strip().split()]
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():

        # 1. Get first node from queue
        current_node = q.get()

        # 2. Get its left child
        left_child = levelorder[index]
        index += 1
        if left_child != -1:
            # make node of left child
            left_node = BinaryTreeNode(left_child)

            # attach it to current node left
            current_node.left = left_node

            # put it in queue
            q.put(left_node)

        # 2. Get its right child
        right_child = levelorder[index]
        index += 1
        if right_child != -1:
            # make node of left child
            right_node = BinaryTreeNode(right_child)

            # attach it to current node left
            current_node.right = right_node

            # put it in queue
            q.put(right_node)

    return root


def PrintLevelWise(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)

    while (not q.empty()):
        # 1.Get curr node from queue
        curr = q.get()
        currData = curr.data

        left = -1

        right = -1
        # 2. check if curr left exist and put it into queue
        if curr.left != None:
            left = curr.left.data
            q.put(curr.left)
        # 2. check if curr right exist and put it into queue
        if curr.right != None:
            right = curr.right.data
            q.put(curr.right)
        # 3. Print currData, left and right
        print(currData, " --> L: ", left, "  R: ", right, sep='')


# root = buildLevelTree()
# PrintLevelWise(root)
