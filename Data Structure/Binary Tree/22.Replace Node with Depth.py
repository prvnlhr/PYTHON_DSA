import BinaryTreeInputPrint


def replaceHelper(root, depth):
    if root is None:
        return None
    root.data = depth

    replaceHelper(root.left, depth + 1)
    replaceHelper(root.right, depth + 1)
    return root


def replaceNodeWithDepth(root):
    root = replaceHelper(root, 0)
    BT.PrintLevelWise(root)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = replaceNodeWithDepth(root)
# BT.PrintLevelWise(root)
