import BinaryTreeInputPrint


# Left Root Right
def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.data, end=' ')
    Inorder(root.right)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
Inorder(root)
