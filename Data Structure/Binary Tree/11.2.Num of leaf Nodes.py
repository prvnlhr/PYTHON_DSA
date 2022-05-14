import BinaryTreeInputPrint

count = 0


def noOfLeafNode(root):
    global count
    if root is None:
        return 0
    if root.left is None and root.right is None:
        count = count + 1

    noOfLeafNode(root.left)
    noOfLeafNode(root.right)
    return count


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = noOfLeafNode(root)
print(ans)
