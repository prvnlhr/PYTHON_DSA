import BinaryTreeInputPrint

result = []


# Reverse Preorder
def rightViewHelper(root, level, max_level):
    global result
    if root is None:
        return []

    # TRICK:
    # At a curr level in tree,
    # we will append that node to result
    # and we will update max_level == curr level
    # so if while recursively traversing , we encounter
    # that our max_level is more then or curr level
    # means we have already visited that level, so we don't need
    # to put that node again in res.
    if max_level[0] < level:
        result.append(root.data)
        max_level[0] = level

    rightViewHelper(root.right, level + 1, max_level)
    rightViewHelper(root.left, level + 1, max_level)


def rightView(root):
    max_level = [0]
    level = 1
    rightViewHelper(root, level, max_level)
    return result


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = rightView(root)
print(result)
# 2 2 13 7 10 1 10 5 2 -1 14 5 11 5 5 13 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 2 3 4 5 -1 7 -1 -1 6 -1 -1 -1 -1 -1
# 1 2 3 4 5 -1 7 -1 -1 6 -1 -1 -1 -1 -1
