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
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


def PrintLevelWise(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    while (not q.empty()):
        curr = q.get()
        currData = curr.data
        left = -1
        right = -1
        if curr.left != None:
            left = curr.left.data
            q.put(curr.left)
        if curr.right != None:
            right = curr.right.data
            q.put(curr.right)
        print(currData, ":L:", left, " R:", right, sep='')


# Examples:
#
# Input:
#       4
#     /   \
#    2      6
#  /  \    /  \
#  1   3  5    7
#
# Output: 1
#       1
#     /   \
#    2      5
#  /  \    /  \
# 3    4  6    7

# 1. Create an array arr[] of size n, where n is the number of nodes in the given BST.
# 2. Perform the inorder traversal of the BST and copy the node values in the arr[] in sorted order.
# 3. Now perform the preorder traversal of the tree.
# 4. While traversing the root during the preorder traversal, one by one copy
#    the values from the array arr[] to the nodes.

def inorder(root, arr):
    if root is None:
        return
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)


# performing preorder traversal
def BSTToMinHeap(root, arr, i):
    if root is None:
        return
    # copying value from array to tree nodes
    i[0] += 1
    root.data = arr[i[0]]
    BSTToMinHeap(root.left, arr, i)
    BSTToMinHeap(root.right, arr, i)


def convertBSTToMinHeap(root):
    arr = []

    inorder(root, arr)

    # used to store index of array for copying nodes
    i = [-1]
    BSTToMinHeap(root, arr, i)


root = buildLevelTree()
convertBSTToMinHeap(root)
PrintLevelWise(root)
