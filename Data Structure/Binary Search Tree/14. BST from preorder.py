import sys

import BST


# Given preorder traversal of a binary search tree, construct the BST.
# For example, if the given traversal is {10, 5, 1, 7, 40, 50},
# then the output should be root of following tree,
# Inorder traversal of the constructed tree is
# 1 5 7 10 40 50
#
class BTN:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# O(N) recursive
def contructTreeFromPreorderRec(preorder):
    def constructTree(preorder, index, MIN, MAX):

        if index == len(preorder):
            return None, index

        currData = preorder[index]

        # if currData out  of range of MIN <-> MAX
        if currData > MIN or currData > MAX:
            return None, index
        # else create root
        root = BTN(currData)

        index = index + 1

        # get root.left and root.right
        root.left, index = constructTree(preorder, index, MIN, currData - 1)
        root.right, index = constructTree(preorder, index, currData + 1, MAX)

        return root, index

    ans = constructTree(preorder, 0, -sys.maxsize, sys.maxsize)
    return ans[0]


# O(N) Solution , using stack

# STEPS:
# STEP__1. Always the first element of preorder array will be root,so make it root of bst
#          and insert it into stack
# STEP__2. now using for loop traverse the preorder array remaining elements from index 1'st not 0'th,
#          and for every element(value) there will be two cases,
#          1. if it is smaller then stack top,
#             then it will be left child of stack top, and insert its value into stack
#          2. if it is greater then stack top,
#             then get the next greater element(last), and make value its right child and append it to stack
# STEP__3. At last return root


# O(N) iterative
def constructTreeIter(preorderArray):
    stack = []

    root = BST.BinaryTreeNode(preorderArray[0])
    stack.append(root)

    for value in preorderArray[1:]:

        if value < stack[-1].data:
            new_left_node = BST.BinaryTreeNode(value)
            stack[-1].left = new_left_node
            stack.append(new_left_node)
        else:
            while stack and stack[-1].data < value:
                last = stack.pop()
            last.right = BST.BinaryTreeNode(value)
            stack.append(last.right)
    return root


preorder = [int(i) for i in input().strip().split()]
bstRoot = contructTreeFromPreorderRec(preorder)
BST.PrintLevelWise(bstRoot)
