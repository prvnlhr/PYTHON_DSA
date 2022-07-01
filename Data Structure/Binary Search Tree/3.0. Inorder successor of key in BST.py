import BST


# REFER STRIVER'S BST VIDEO YOUTUBE


# T:O(H) and S: O(1)
def inorderPredecessor(root, key):
    predecessor = None

    while root != None:
        if root.data >= key:
            root = root.left
        else:
            predecessor = root.data
            root = root.right

    return predecessor


def inorderSuccessor(root, key):
    successor = None

    while root != None:
        if root.data > key:
            successor = root.data
            root = root.left
        else:
            root = root.right

    return successor


root = BST.buildLevelTree()
key = int(input())
succ = inorderSuccessor(root, key)
pre = inorderPredecessor(root, key)
print('successor:', succ, 'predecessor:', pre)
# 20 10 30 5 15 25 35 -1 7 13 18 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
