import BST
import sys

min = sys.maxsize
max = ~sys.maxsize


def findMinMax(root):
    global max
    global min
    if root is None:
        return None

    if root.data > max:
        max = root.data
    if root.data < min:
        min = root.data

    findMinMax(root.left)
    findMinMax(root.right)
    return min, max


root = BST.buildLevelTree()
ans = findMinMax(root)
print(ans)
