import BinaryTreeInputPrint
import sys

min = sys.maxsize
max = ~sys.maxsize


def findMaxMinNode(root):
    global max
    global min

    if root is None:
        return None

    if root.data > max:
        max = root.data
    if root.data < min:
        min = root.data
    findMaxMinNode(root.left)
    findMaxMinNode(root.right)
    return max, min


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
max, min = findMaxMinNode(root)
print(max, min)
# BT.PrintLevelWise(root)
