import BST


# To find the median, we need to find the Inorder of the BST because
# its Inorder will be in sorted order and then find the median i.e.
# The idea is based on K’th smallest element in BST using O(1) Extra Space
# The task is very simple if we are allowed to use extra space but Inorder
# traversal using recursion and stack both uses Space which is not allowed here.
# So, the solution is to do Morris Inorder traversal as it doesnt require any extra space.

def morrisInorderTraversal(root):
    sol = []

    curr = root

    while curr is not None:  # This Means we have reached Right Most Node i.e end of LDR traversal
        if curr.left is not None:
            pre = curr.left
            while pre.right is not None and pre.right != curr:
                pre = pre.right
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                sol.append(curr.data)
                pre.right = None
                curr = curr.right
        else:
            sol.append(curr.data)
            curr = curr.right

    return sol


def findMedian(inorderTravesal):
    l = len(inorderTravesal)
    mid = l // 2
    if l % 2 == 0:
        a = inorderTravesal[mid]
        b = inorderTravesal[mid - 1]
        median = (a + b) // 2
        return median

    else:
        median = inorderTravesal[mid]
        return median


root = BST.buildLevelTree()
ans = morrisInorderTraversal(root)
median = findMedian(ans)
print(median)
