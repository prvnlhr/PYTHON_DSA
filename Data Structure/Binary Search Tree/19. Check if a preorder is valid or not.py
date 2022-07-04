import sys

import BST


# METHOD 1_. NAIVE APPROACH ::
# To check if a sequence of preorder is valid or not
# we can build a tree from preorder array and then find its
# inorder traversal, and then check if inorder is increasing
# or not which will conclude if its BST or not.


# METHOD 2_. There is one more solution using stack

# METHOD 3_. O(N) Solution using MIN MAX approach
# Will use same concept, we used to build BST using
# MIN MAX concept, but we will not build tree, but traversed
# the whole preorder sequence
# At end we will see if the whole sequence is traversed or
# still remaining ,thus we can conclude if sequence is valid or not


# O(N) recursive
class BTN:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTreeFromPreorder(preorder):

    def helper(preorder, index, MIN, MAX):
        if index >= len(preorder):
            return None, index

        currData = preorder[index]
        # if currData out  of range of MIN <-> MAX
        if MIN > currData or currData > MAX:
            return None, index

        root = BTN(currData)
        index = index + 1

        root.left, index = helper(preorder, index, MIN, currData - 1)
        root.right, index = helper(preorder, index, currData + 1, MAX)
        return root, index

    ans = helper(preorder, 0, -sys.maxsize, sys.maxsize)
    print(ans[1])

    if ans[1] == len(preorder):
        return 'Valid'
    else:
        return 'Invalid'


preorder = [int(i) for i in input().strip().split()]
isValid = buildTreeFromPreorder(preorder)
print(isValid)
# BST.PrintLevelWise(bstRoot)
