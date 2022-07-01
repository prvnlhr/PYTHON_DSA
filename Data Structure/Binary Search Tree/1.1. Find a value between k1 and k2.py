import BST

result = []


def findBtwK1K2(root, k1, k2):
    res = []

    def findAll(root):
        if root is None:
            return None
        print(k1, root.data, k2)
        if root.data > k1 and root.data < k2:
            res.append(root.data)
            findAll(root.left)
            findAll(root.right)
        elif root.data >= k2:
            findAll(root.left)
        elif root.data <= k1:
            findAll(root.right)

    findAll(root)
    return res


def findELementsBtwK1K2(root, k1, k2):
    # ______________________________________________________________________
    if root is None:
        return
        # if root.data < k1:
    if root.data < k1:
        findELementsBtwK1K2(root.right, k1, k2)
    elif root.data > k2:
        findELementsBtwK1K2(root.left, k1, k2)

    # else root.data is between k1 and k2
    else:
        result.append(root.data)
        findELementsBtwK1K2(root.left, k1, k2)
        findELementsBtwK1K2(root.right, k1, k2)


# ______________________________________________________________________


root = BST.buildLevelTree()
k1, k2 = (int(i) for i in input().strip().split())
# ans = findELementsBtwK1K2(root, k1, k2)
ans = findBtwK1K2(root, k1, k2)
print(ans)
