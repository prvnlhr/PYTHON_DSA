import BinaryTreeInputPrint


def pathSumHelperCN(root, x, path, currSum):
    if root is None:
        return None

    if root.left is None and root.right is None:
        currSum = currSum + root.data

        if currSum == x:
            print(str(path + str(root.data) + ' ').lstrip())
        return
    pathSumHelperCN(root.left, x, str(path + str(root.data) + ' '), currSum + root.data)
    pathSumHelperCN(root.right, x, str(path + str(root.data) + ' '), currSum + root.data)


def pathSumHelperLeetcode(root, sum, path, result):
    if root is None:
        return None

    if root.data == sum and root.left is None and root.right is None:
        result.append([*path, root.data])
        print(result)
        return None

    path.append(root.data)
    pathSumHelperLeetcode(root.left, sum - root.data, path, result)
    pathSumHelperLeetcode(root.right, sum - root.data, path, result)
    path.pop()


def pathSum(root, sum):
    result = []
    # pathSumHelperLeetcode(root, sum, [], result)
    pathSumHelperCN(root, sum, ' ', 0)
    return result


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
sum = int(input())
ans = pathSum(root, sum)
print(ans)
# BT.PrintLevelWise(root)
