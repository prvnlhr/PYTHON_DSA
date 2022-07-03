# SOLUTION:
# https://leetcode.com/problems/delete-node-in-a-bst/discuss/821420/Python-O(h)-solution-explained

class Solution:
    def deleteNode(self, root, key):

        # base case
        if not root:
            return None

        # __base case (almost) with key found
        if root.data == key:

            # 1.a leaf or single child,only left child exists
            if not root.right:
                return root.left

            # 1.b leaf or single child,only right child exists
            if not root.left:
                return root.right

            # 2: both child node exist
            if root.left and root.right:
                # 2.a.1: start with right node of deleted node
                temp = root.right

                # 2.a.2: find minimum node in left subtree
                # we are going to replace minimum in left subtree with value at root
                while temp.left:
                    temp = temp.left

                # 2.b: replace value with minimum value in right subtree
                root.data = temp.data

                # 2.c: ** key step ** recurse on root.right but with key = root.data (min val in right subtree)
                root.right = self.deleteNode(root.right, root.data)

        # __recursion steps
        elif root.data > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
