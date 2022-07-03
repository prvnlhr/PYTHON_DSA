import BST


# 1. Initialize current as root
# 2. While current is not NULL
#    If the current does not have left child
#       a) Print current’s data
#       b) Go to the right, i.e., current = current->right
#    Else
#       a) Find rightmost node in current left subtree OR node whose right child == current.
#          If we found , right child == current
#              a) Update the right child as NULL of that node whose right child is current
#              b) Print current’s data
#              c) Go to the right, i.e. current = current->right
#          Else
#              a) Make current as the right child of that rightmost
#                 node we found; and
#              b) Go to this left child, i.e., current = current->left


# Time Complexity : O(n) If we take a closer look, we can notice that every
# edge of the tree is traversed at most three times. And in the worst case,
# the same number of extra edges (as input tree) are created and removed.

def morrisInorderTraversalx(root):
    sol = []

    curr = root

    while curr is not None:  # This Means we have reached Right Most Node i.e end of LDR traversal

        if curr.left is not None:
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                sol.append(curr.data)
                pre.right = None
                curr = curr.right
        else:
            sol.append(curr.data)
            curr = curr.right

    return sol


# STRIVER'S SOLUTION YOUTUBE

def morrisInorderTraversal(root):
    # output array
    inorder = []
    curr = root
    # initialize curr as root
    while curr is not None:  # This Means we have reached Right Most Node i.e end of LDR traversal

        # STEP 1__. Check curr.left is None or not ?

        # if None --> curr is traversal node so append it to output array,
        # and move to right of curr
        if curr.left is None:
            inorder.append(curr.data)
            curr = curr.right
        # if not none --> find its right most node
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            # if right most node is None then connect it to curr
            if prev.right is None:
                # make thread
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                inorder.append(curr.data)
                curr = curr.right

    return inorder


root = BST.buildLevelTree()
ans = morrisInorderTraversal(root)
# ans = morrisInorderTraversalx(root)
print(ans)
# Ex__
# input -> 1 2 3 4 5 -1 -1 -1 -1 -1 6 -1 -1
# output-> [4, 2, 5, 6, 1, 3]
