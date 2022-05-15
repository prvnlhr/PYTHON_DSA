import copy

import BinaryTreeInputPrint


# Find all path root-to-leaf that sums to given sum
# Ex_5 4 8 11 -1 -1 4 7 2 5 1 -1 -1 -1 -1 3 6 -1 -1 -1 -1 -1 -1
# sum = 22
# there are two path whose sum == 22
# but the second one does not terminate with leaf node
# ['5 4 11 2']
# ['5 8 4 5']
#
def pathSum(root, sum):
    def findPath(root, sum, path):
        if root is None:
            return []
        print(sum, root.data)
        path = path + str(root.data)
        # if sum == root.data and root.left is None and root.right is None:
        if sum == root.data:
            return [path]
        path = path + ' '
        return findPath(root.left, sum - root.data, path) + findPath(root.right, sum - root.data, path)

    return findPath(root, sum, '')


def pathSum1(root, sum):
    if root is None:
        return ''
    if root.data == sum and root.left is None and root.right is None:
        return True
    pathSum(root.left, sum - root.data) + pathSum(root.right, sum - root.data)


# final_______________________________________
def pathSumToK(root, k):
    res = []

    def findPath(root, sum, path):
        if root is None:
            return None

        path.append(root.data)
        if sum == root.data and root.left is None and root.right is None:
            res.append(copy.deepcopy(path))
        findPath(root.left, sum - root.data, path)
        findPath(root.right, sum - root.data, path)
        path.pop()

    findPath(root, k, [])
    return res


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
sum = int(input())
ans = pathSum(root, sum)
print(ans)
# BT.PrintLevelWise(root)
