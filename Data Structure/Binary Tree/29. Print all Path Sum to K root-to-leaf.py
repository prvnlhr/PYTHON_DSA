import BinaryTreeInputPrint


# Given the root of a binary tree and an integer
# targetSum, return true if the tree has a root-to-leaf
# path such that adding up all the values along the
# path equals targetSum.
# A leaf is a node with no children.
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
#

def pathSum(R, S):
    A, P = [], []

    def dfs(N):
        if N == None: return
        P.append(N.data)
        if (N.left, N.right) == (None, None) and sum(P) == S:
            A.append(list(P))
        else:
            dfs(N.left), dfs(N.right)
        P.pop()

    dfs(R)
    return A


res = []


def sumPath(root, s, path):
    global res
    if root is None:
        return ''

    path += str(root.data)

    if s == root.data and root.left is None and root.right is None:
        res.append(path)

    path = path + ' '

    sumPath(root.left, s - root.data, path)
    sumPath(root.right, s - root.data, path)
    return res


def pathSum(root, s):
    path, ans = [], []

    def getPath(root):
        if root is None:
            return None

        path.append(root.data)

        if root.left is None and root.right is None and sum(path) == s:
            ans.append(list(path))
        else:
            getPath(root.left)
            getPath(root.right)
        path.pop()

    getPath(root)
    return ans


BT = BinaryTreeInputPrint
# 5 4 8 11 -1 13 4 7 2 -1 -1 5 1 -1 -1 -1 -1 -1 -1 -1 -1
# 22
root = BT.buildLevelTree()
s = int(input())
# ans = sumPath(root, s, '')
ans = pathSum(root, s)
print(ans)
