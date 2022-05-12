import BinaryTreeInputPrint


def findPath(root, n, path):
    if root is None:
        return False
    path.append(root.data)

    if root.data == n:
        return True

    if (root.left and findPath(root.left, n, path)) or (root.right and findPath(root.right, n, path)):
        return True

    path.pop()
    return False


def LCA(root, n1, n2):
    path1 = []
    path2 = []
    findPath(root, n1, path1)
    findPath(root, n2, path2)
    print(path1)
    print(path2)
    i = 0
    while i < len(path1) and i < len(path2):

        if path1[i] != path2[i]:
            break
        i = i + 1
    return path1[i - 1]


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
n1 = int(input())
n2 = int(input())
ans = LCA(root, n1, n2)
print(ans)
