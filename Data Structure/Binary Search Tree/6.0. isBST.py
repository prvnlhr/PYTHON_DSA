import BST
import sys


# O(n * n) worst case
def isBST(root):
    if root is None:
        return True

    leftMax = maximum(root.left)

    if leftMax >= root.data:
        return False

    rightMin = minimum(root.right)

    if rightMin < root.data:
        return False

    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)

    return isLeftBST and isRightBST


def minimum(root):
    if root is None:
        return sys.maxsize

    leftMin = minimum(root.left)
    rightMin = minimum(root.right)
    return min(root.data, min(leftMin, rightMin))


def maximum(root):
    if root is None:
        return -1

    leftMax = maximum(root.left)
    rightMax = maximum(root.right)
    return max(root.data, max(leftMax, rightMax))


root = BST.buildLevelTree()

ans = isBST(root)
print(ans)
