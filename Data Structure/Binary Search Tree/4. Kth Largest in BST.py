import BST


# reverse inorder
def kthLargest(root, k):
    # NOTE WE ARE USING GLOBAL
    # VALUE OF K AS WE DON'T
    # WANT VALUE OF K TO DECREASE
    # IN EVERY RECURSIVE CALL
    # WE WANT IT TO DECREASE IN REVERSE CALLING ONLY

    def find(root):
        global k
        if root is None:
            return None

        right = find(root.right)

        if right != None:
            return right

        k = k - 1

        # if kth largest  node reached
        if k == 0:
            return root
        return find(root.left)

    return find(root)


root = BST.buildLevelTree()
k = int(input())
ans = kthLargest(root, k)
