import BinaryTreeInputPrint


def heightOfBt(root):
    if root is None:
        return 0

    lh = heightOfBt(root.left)
    rh = heightOfBt(root.right)
    return 1 + max(lh, rh)


# Main____
BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = heightOfBt(root)
print(ans)
# BT.PrintLevelWise(root)
