import BinaryTreeInputPrint


# Left Right Root
def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=' ')


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
postOrder(root)
