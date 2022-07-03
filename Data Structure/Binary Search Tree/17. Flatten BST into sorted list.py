import BST


# You have been given a Binary Search Tree (BST). Your task is to flatten the given
# BST to a sorted list. More formally, you have to make a right-skewed BST from
# the given BST, i.e., the left child of all the nodes must be NULL, and the
# value at the right child must be greater than the current node.


def flattenBST(root):
    if root is None:
        return None

    dummy = BST.BinaryTreeNode(-1)
    prev = dummy

    def buildTree(curr):
        nonlocal prev

        if curr is None:
            return None

        buildTree(curr.left)

        # All magic happens here,
        prev.left = None
        prev.right = curr
        prev = curr
        buildTree(curr.right)

    buildTree(root)

    prev.left = None
    prev.right = None
    newRoot = dummy.right
    return newRoot


# def flattenBSTHelper(curr):
#     global prev
#     if curr is None:
#         return
#     flattenBSTHelper(curr.left)
#     prev.left = None
#     prev.right = curr
#     prev = curr
#     flattenBSTHelper(curr.right)
#
#
# def flattenBST(root):
#     global prev
#     if root is None:
#         return
#     dummy = BST.BinaryTreeNode(-1)
#     prev = dummy
#     flattenBSTHelper(root)
#     prev.left = None
#     prev.right = None
#     ret = dummy.right
#     return ret


root = BST.buildLevelTree()
newRoot = flattenBST(root)
BST.PrintLevelWise(newRoot)
