import BinaryTreeInputPrint


def nodeWithSiblings(root):
    if root is None:
        return

    if root.left and root.right:
        nodeWithSiblings(root.left)
        nodeWithSiblings(root.right)

    elif root.left and root.right is None:
        print(root.left.data)
        nodeWithSiblings(root.left)
    elif root.right and root.left is None:
        print(root.right.data)
        nodeWithSiblings(root.right)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = nodeWithSiblings(root)
