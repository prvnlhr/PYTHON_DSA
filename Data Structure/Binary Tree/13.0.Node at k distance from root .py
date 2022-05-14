import BinaryTreeInputPrint

res = []


def nodesAtKDistance(root, k):
    res = []

    def findNodes(root, k):
        if root is None:
            return None
        if k == 0:
            res.append(root.data)
        findNodes(root.left, k - 1)
        findNodes(root.right, k - 1)

    findNodes(root, k)
    return res


# 1 2 3 4 5 -1 8 17 -1 6 7 -1 9 -1 -1 -1 -1 10 12 -1 -1 -1 -1 14 -1 -1 -1
BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
k = int(input())
ans = nodesAtKDistance(root, k)
print(ans)
