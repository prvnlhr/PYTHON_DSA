import BST


def findPreSuc(root, key):
    pred = [None]
    succ = [None]

    def find(root, key):
        if root is None:
            return None
        find(root.left, key)

        if root and root.data < key:
            pred[0] = root

        elif root and root.data > key:
            if not succ[0]:
                succ[0] = root
            elif succ[0] and succ[0].data > root.data:
                succ[0] = root

        find(root.right, key)
        return pred, succ

    return find(root, key)


def findPreSucc(root, key):
    pred = [None]
    succ = [None]

    # Well this solution does look scary, but its pretty easy
    # We are just doing inorder traversal
    # so we are going to left most node first then
    # checking if root is smaller or greater then key,
    # if smaller then assign it to p
    # if larger then assign it to q ,but check if previously assigned is greater or not

    def preSucc(root, key):

        if root is None:
            return

        # __recur left most node
        preSucc(root.left, key)

        # Condition 1. if root is greater then key
        if root and root.data > key:
            # only assign if previous data is larger
            if ((not succ[0]) or succ[0] and succ[0].data > root.data):
                succ[0] = root

        # Condition 2. if root is smaller then key
        elif root and root.data < key:
            pred[0] = root

        # recur right tree
        preSucc(root.right, key)
        return pred, succ

    return preSucc(root, key)


# 18 10 19 5 13 -1 22 4 6 12 14 20 25 -1 -1 -1 -1 11 -1 -1 15 -1 -1 23 -1 -1 -1 -1 -1 -1 -1
root = BST.buildLevelTree()
key = 12
ans = findPreSuc(root, key)
print(ans[0][0].data, ans[1][0].data)
