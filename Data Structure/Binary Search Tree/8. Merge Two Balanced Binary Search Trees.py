import BST


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# You are given two balanced binary search trees e.g., AVL or Red Black Tree.
# Write a function that merges the two given balanced BSTs into a balanced binary search tree.
# Let there be m elements in first tree and n elements in the other tree.
# Your merge function should take O(m+n) time.

# Method 2 (Merge Inorder Traversals)
# 1) Do inorder traversal of first tree and store the traversal in one temp array arr1[]. This step takes O(m) time.
# 2) Do inorder traversal of second tree and store the traversal in another temp array arr2[]. This step takes O(n) time.
# 3) The arrays created in step 1 and 2 are sorted arrays. Merge the two sorted arrays into one array of size m + n. This step takes O(m+n) time.
# 4) Construct a balanced tree from the merged array using the technique discussed in this post. This step takes O(m+n) time.
# Time complexity of this method is O(m+n) which is better than method 1. This method takes O(m+n) time even if the input BSTs are not balanced.


# STEP 1:____________________________________________________________
def createSortedArray_from_BST(root, arr=[]):
    if root is None:
        return None

    createSortedArray_from_BST(root.left, arr)
    arr.append(root.data)
    createSortedArray_from_BST(root.right, arr)
    return arr


# STEP 2:____________________________________________________________
def mergeSortedArray(arr1, arr2):
    i = 0
    j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i = i + 1
        else:
            arr.append(arr2[j])
            j = j + 1
    while i < len(arr1):
        arr.append(arr1[i])
        i = i + 1
    while j < len(arr2):
        arr.append(arr2[j])
        j = j + 1
    return arr


# STEP 3:____________________________________________________________
def sortedArrayToBST(arr):
    if not arr:
        return None

    mid = len(arr) // 2

    root = BinaryTreeNode(arr[mid])

    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid + 1:])

    return root


root1 = BST.buildLevelTree()
root2 = BST.buildLevelTree()
arr1 = []
createSortedArray_from_BST(root1, arr1)
arr2 = []
createSortedArray_from_BST(root2, arr2)
arr = mergeSortedArray(arr1, arr2)
root = sortedArrayToBST(arr)

BST.PrintLevelWise(root)
