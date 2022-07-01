import BST


def findAValue(root, x):
    if root is None:
        return None

    if root.data == x:
        return "YES"

    if root.data < x:
        return findAValue(root.right, x)
    else:
        return findAValue(root.left, x)


root = BST.buildLevelTree()
x = int(input())
ans = findAValue(root, x)
print(ans)

# BST.PrintLevelWise(root)
