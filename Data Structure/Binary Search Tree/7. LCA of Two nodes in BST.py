import BST


# AS it is BST, lCA of two nodes(n1,n2) can be either in left subtree or right subtree
# so compare n1 and n2 to root node, if root is greater then n1 and n2,
# lCA is in left subtree so recur root.left
# if root is smaller then n1 and n2, lca is in right subtree, recur right subtree
# if root lies between n1 and n2, i.e above two conditions doesnt satisfies, then root is LCA.

def LCA(root, n1, n2):
    if root is None:
        return None

    # If n1 and n2 both are smaller then root,
    # then they lies in left subtree
    if root.data > n1 and root.data > n2:
        LCA(root.left, n1, n2)

    # if n1 and n2 both are greater then root,
    # they lies in right subtree
    if root.data < n1 and root.data < n2:
        LCA(root.right, n1, n2)

    # else root is lca , return it,
    return root


root = BST.buildLevelTree()

n1 = int(input())
n2 = int(input())
ans = LCA(root, n1, n2)
print(ans.data)
