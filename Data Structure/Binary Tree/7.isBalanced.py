import BinaryTreeInputPrint


# A balanced binary tree is also known as height balanced tree.
# It is defined as binary tree in when the difference between
# the height of the left subtree and right subtree is not more than m,
# where m is usually equal to 1. The height of a tree is the number
# of edges on the longest path between the root node and the leaf node.


# __O(n^2):
def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh, rh)


def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False

    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)

    if isRightBalanced and isLeftBalanced:
        return True


# __final O(n) and also seems a easy solution :
def isBalancedAndHeight(root):
    if root is None:
        return 0, True

    lh, isLeftBalanced = isBalancedAndHeight(root.left)
    rh, isRightBalanced = isBalancedAndHeight(root.right)
    h =  max(lh, rh)

    if lh - rh > 1 or rh - lh > 1:
        return h+1, False
    else:
        return h+1, True


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = isBalancedAndHeight(root)
print(ans)
# BT.PrintLevelWise(root)
