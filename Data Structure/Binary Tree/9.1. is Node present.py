import BinaryTreeInputPrint


def isNodePresent(root, x):
    if root is None:
        return None
    print(root.data, x)
    if root.data == x:
        return 'Yes'
    return isNodePresent(root.left, x) or isNodePresent(root.right, x)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
x = int(input())
ans = isNodePresent(root, x)
print(ans)
