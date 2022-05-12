import BinaryTreeInputPrint

# For a given Binary Tree of integers, find and return the sum of all the nodes data.
# Sample Input 1:
# 2 3 4 6 -1 -1 -1 -1 -1
# Sample Output 1:
#  15
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Sample Output 2:
#  28


sum = 0


def sumOfBT(root):
    global sum
    if root is None:
        return 0

    sum = sum + root.data

    sumOfBT(root.left)
    sumOfBT(root.right)
    return sum


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ans = sumOfBT(root)
print(ans)
