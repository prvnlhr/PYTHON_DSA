import BinaryTreeInputPrint


# For a given Binary Tree of type integer, update
# it with its corresponding mirror image.

# __ O(N)
def mirrorTree(root):
    if root is None:
        return

    # recur on left and right sub tree
    mirrorTree(root.left)
    mirrorTree(root.right)

    # if both left and right exists, swap
    if root.left and root.right:
        root.left.data, root.right.data = root.right.data, root.left.data


# self solved worked perfectly O(N)
def mirrorTree(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    if root.left is not None and root.right is not None:
        temp = root.left
        root.left = root.right
        root.right = temp

    elif root.left is None:
        root.left = root.right
        root.right = None
    elif root.right is None:
        root.right = root.left
        root.left = None
    mirrorTree(root.left)
    mirrorTree(root.right)
    return root


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
mirrorTree(root)
BT.PrintLevelWise(root)
