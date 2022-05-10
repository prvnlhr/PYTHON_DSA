import BinaryTreeInputPrint


# Root Left Right
def preOrder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
preOrder(root)
