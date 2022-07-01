import copy
import sys

import BST


def isBST(root):
    def isBSTHelper(root, MIN, MAX):
        if root is None:
            return True
        print(MIN, root.data, MAX)

        if root.data > MAX or root.data < MIN:
            return False

        a = isBSTHelper(root.left, MIN, root.data - 1)
        b = isBSTHelper(root.right, root.data + 1, MAX)
        return a and b

    return isBSTHelper(root, float('-inf'), float('inf'))


root = BST.buildLevelTree()
'''
18 10 19 5 13 -1 22 4 6 12 14 20 25 -1 -1 -1 -1 21 -1 -1 15 -1 -1 23 -1 -1 -1 -1 -1 -1 -1
'''
ans = (isBST(root))
print(ans)
