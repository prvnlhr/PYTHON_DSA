import BinaryTreeInputPrint


# This is a typical tree traversal question. We start from
# the root and check if the node has one child, if yes
# then print the only child of that node. If the node has
# both children, then recur for both the children

def nodeWithSiblings(root):
    if root is None:
        return

    # if node has both children recur on both
    if root.left and root.right:
        nodeWithSiblings(root.left)
        nodeWithSiblings(root.right)

    # if only left child,means no sibling,print and recur on left child
    elif root.left and root.right is None:
        print(root.left.data)
        nodeWithSiblings(root.left)

    # if only right child,means no sibling,print and recur on right child
    elif root.right and root.left is None:
        print(root.right.data)
        nodeWithSiblings(root.right)


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = nodeWithSiblings(root)
