# POINTS TO REMEMBER:
# Inorder traversal of BST gives sorted array.
import BST


def constructBST(sortedArr):
    if len(sortedArr) <= 0:
        return None
    # get middle index and middle element
    middle_distance = len(sortedArr) // 2
    middle_element = sortedArr[middle_distance]
    # create node from middle element
    root = BST.BinaryTreeNode(middle_element)
    # recur from 0 to mid  and   mid+1 to len-1
    root.left = constructBST(sortedArr[:middle_distance])
    root.right = constructBST(sortedArr[middle_distance + 1:])
    return root


def printPreorder(root):
    if root is None:
        return None
    print(root.data, end=' ')
    printPreorder(root.left)
    printPreorder(root.right)


sorted_Arr = [int(i) for i in input().strip().split()]
root = constructBST(sorted_Arr)
printPreorder(root)
# BST.PrintLevelWise(root)
