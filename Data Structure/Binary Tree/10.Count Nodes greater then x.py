import BinaryTreeInputPrint

#
count = 0


def nodesGreaterThenX(root, x):
    global count
    if root is None:
        return 0
    if root.data > x:
        count = count + 1
    nodesGreaterThenX(root.left, x)
    nodesGreaterThenX(root.right, x)
    return count


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
x = int(input())
ans = nodesGreaterThenX(root, x)
print(ans)
