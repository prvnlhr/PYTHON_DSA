import sys

import BST

# Given a Binary search Tree that contains positive integer values greater than 0.
# The task is to check whether the BST contains a dead end or not.
# Here Dead End means, we are not able to insert any element after that node.
# Input :        8
#              /   \
#             5     9
#           /  \
#         2     7
#        /
#       1

# Output : Yes
# Explanation : Node "1" is the dead End because after that we cant insert any element.
#
# Input :       8
#             /   \
#            7    10
#          /     /  \
#         2     9    13
#
# Output : Yes
# Explanation : We can't insert any element at node 9.
#
# IMPLEMENTATION:___________________________________
# If we take a closer look at the problem, we can notice that we
# basically need to check if there is a leaf node with value x
# such that x + 1 and x - 1 exist in BST with the exception of x = 1. For x = 1,
# we can’t insert 0 as the problem statement says BST contains positive integers only.
# To implement the above idea we first traverse the whole BST and store all nodes
# in a hash_map.We also store all leaves in a separate hash to avoid re-traversal of BST.
# Finally, we check for every leaf node x, if x-1 and x+1 are present in hash_map or not.

all_nodes = set()
leaf_nodes = set()


def storeInSets(root):
    global all_nodes
    global leaf_nodes

    if root == None:
        return

    # for all nodes insert root in all_nodes set
    all_nodes.add(root.data)

    # for leaf node insert in set of leaf_nodes
    if root.left == None and root.right == None:
        leaf_nodes.add(root.data)
        return

    # recur for left and right subtree
    storeInSets(root.left)
    storeInSets(root.right)


def isDeadEnd(root):
    if root is None:
        return False

    all_nodes.add(0)

    # All magic happens here, we are checking for dead ends
    for x in leaf_nodes:
        if x + 1 in all_nodes and x - 1 in all_nodes:
            return True
    return False


# O(N) Recursive solution,Simple
def containsDeadEnds(root):
    MIN, MAX = -sys.maxsize, sys.maxsize

    def findDeadEnds(root, MIN, MAX):
        if root is None:
            return False

        if MIN == MAX:
            return True

        a = findDeadEnds(root.left, MIN, root.data - 1)
        b = findDeadEnds(root.right, root.data + 1, MAX)
        return a or b

    return findDeadEnds(root, MIN, MAX)


root = BST.buildLevelTree()

ans = isDeadEnd(root)
# ans = containsDeadEnds(root)
print(ans)
