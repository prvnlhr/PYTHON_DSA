import BinaryTreeInputPrint


def removeLeafNodes(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        root.data = None
    removeLeafNodes(root.left)
    removeLeafNodes(root.right)
    return root


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
root = removeLeafNodes(root)
BT.PrintLevelWise(root)
