import BinaryTreeInputPrint


# Given a binary tree, print boundary nodes of the binary tree
# Anti-Clockwise starting from the root. The boundary includes
# left boundary, leaves, and right boundary in order without
# duplicate nodes. (The values of the nodes may still be duplicates.)
# The LEFT BOUNDARY is defined as the path from the root to the
# left-most node. The RIGHT BOUNDARY is defined as the path from
# the root to the right-most node. If the root doesn't have left
# subtree or right subtree, then the root itself is left boundary
# or right boundary. Note this definition only applies to the input
# binary tree, and not apply to any subtrees.
# The LEFT_MOST node is defined as a leaf node you could reach
# when you always firstly travel to the left subtree if it exists.
# If not, travel to the right subtree. Repeat until you reach a leaf node.
# The right-most node is also defined in the same way with left and right exchanged.
#
# INTUITION :
# Every tree's boundary traversal consists of following node,
# __root node
# __left boundary node
# __right boundary nodes
# __left subtree leaf nodes
# __right subtree leaf nodes

def printLeafNodes(root):
    if root is None:
        return
    printLeafNodes(root.left)
    if root.left is None and root.right is None:
        print(root.data, end=" ")
    printLeafNodes(root.right)


def printLeftBoundary(root):
    if root is None:
        return
    if root.left is not None:
        print(root.data, end=" ")
        printLeftBoundary(root.left)
    # now , why we are calling on right node ,because there can be
    # a case where a zig zig alignment is there,
    # Ex__1 2 3 4 5 6 7 -1 8 -1 -1 -1 -1 -1 -1 9 -1 -1 10 -1 -1
    elif root.right is not None:
        print(root.data, end=" ")
        printLeftBoundary(root.right)


def printRightBoundary(root):
    if root is None:
        return
    if root.right is not None:
        printRightBoundary(root.right)
        print(root.data, end=" ")
    elif root.left is not None:
        printRightBoundary(root.left)
        print(root.data, end=" ")


def printBoundary(root):
    if root is None:
        return

    print(root.data,end=" ")
    # print(' ')

    printLeftBoundary(root.left)
    # print(' ')
    printLeafNodes(root.left)
    # print(' ')
    printLeafNodes(root.right)
    # print(' ')
    printRightBoundary(root.right)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
printBoundary(root)
# 20  8  4 10 14  25  22