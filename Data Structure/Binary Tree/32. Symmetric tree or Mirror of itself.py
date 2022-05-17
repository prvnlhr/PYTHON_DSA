import BinaryTreeInputPrint


# Ex_1
#         1
#       /   \
#      2     2
#     / \   / \
#    3   4 4   3
#   True
#
# Ex_2
#        1
#       / \
#      2   2
#       \   \
#       3    3
#   False

def mirrorOfItsself(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 and root2:
        if root1.data == root2.data:
            left1Right2Mirror = mirrorOfItsself(root1.left, root2.right)
            right1Left2Mirror = mirrorOfItsself(root1.right, root2.left)
            return left1Right2Mirror and right1Left2Mirror
    return False


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = mirrorOfItsself(root, root)
print(ans)
