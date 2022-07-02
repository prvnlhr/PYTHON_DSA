import BST


# Inorder
def kthSmallest(root, k):
    # NOTE WE ARE USING GLOBAL
    # VALUE OF K AS WE DON'T
    # WANT VALUE OF K TO DECREASE
    # IN EVERY RECURSIVE CALL
    # WE WANT IT TO DECREASE IN REVERSE CALLING ONLY

    def find(root):

        nonlocal k

        if root is None:
            return

        left = find(root.left)

        if left != None:
            return left

        k = k - 1

        # if kth smallest  node reached
        if k == 0:
            return root

        return find(root.right)

    return find(root)


root = BST.buildLevelTree()
k = int(input())
ans = kthSmallest(root, k)
print(ans.data)
