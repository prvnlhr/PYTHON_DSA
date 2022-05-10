import BinaryTreeInputPrint


# The diameter of a tree can be defined as the maximum
# distance between two leaf nodes.
# Here, the distance is measured in terms of the total
# number of nodes present along the path of the two leaf nodes, including both the leaves.
#
# The diameter of a tree T is the largest of the following quantities:
# __the diameter of T’s left subtree.
# __the diameter of T’s right subtree.
# __the longest path between leaves that goes,
# __through the root of T (this can be computed from the heights of the subtrees of T)
#
# Diameter is total distance between leaf nodes of left-subtree and right-subtree
# which is maximum
# Solution:: we find the left-subtree depth and right-subtree depth,
# So total depth is l + r + 1, if it is max when compare to prev ans we update it
# and then we return max of l ,r  + 1 for next iteration


# __________OR____________________________
def dia(root):
    ans = [0]

    def depth(root):
        if root is None:
            return 0

        l = depth(root.left)
        r = depth(root.right)
        dia = l + r + 1
        ans[0] = max(ans[0], dia)
        return max(l, r) + 1

    depth(root)
    return ans[0]


# _________________________________________________
def heightTree(root, ans):
    if root == None:
        return 0
    lh = heightTree(root.left, ans)
    rh = heightTree(root.right, ans)
    ans[0] = max(ans[0], 1 + lh + rh)
    return 1 + max(lh + rh)


# Optimised O(n)____
def diameterOfTree(root):
    if root == None:
        return 0
    ans = [-999999]
    heightOfTree = heightTree(root, ans)
    return ans[0]


# ___________________________________________________
def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh, rh)


# O(n^2)___
def diameter(root):
    lhMax = height(root.left)
    rhMax = height(root.right)

    ld = diameter(root.left)
    rd = diameter(root.right)

    h = lhMax + rhMax + 1
    dia = max(h, rd, ld)
    return dia


# Leetcode Sol O(n):
ans = 1


def diameterOfTree(root):
    ans = [0]

    def depth(root):
        if root is None:
            return 0
        # find depth of left and right subtree
        l = depth(root.left)
        r = depth(root.right)
        # total depth is (l + r + 1)
        # compare it with ans if max update ans
        ans[0] = max(ans[0], l + r + 1)
        # and return max depth from (l , r) + 1
        # this basically we, returning height
        return max(l, r) + 1

    depth(root)
    return ans[0]


# Main____________________________________________________________________


# 1 2 3 4 5 -1 -1 -1 -1 -1 -1
# 1 2 3 4 5 -1 8 -1 -1 6 7 -1 9 -1 -1 -1 -1 10 11 -1 12 -1 -1 -1 -1
# 1 2 3 4 5 -1 -1 10 11 -1 7 -1 -1 12 -1 8 7 -1 13 -1 -1 10 -1 -1 -1 -1 -1
# 1 2 3 4 5 6 7 -1 8 -1 -1 -1 -1 -1 -1 9 -1 -1 10 -1 -1

BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = diameterOfTree(root)
print(ans)
