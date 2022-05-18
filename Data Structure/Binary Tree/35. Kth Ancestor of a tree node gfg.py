import BinaryTreeInputPrint


# 1 2 3 4 5 8 9 -1 -1 6 7 -1 -1 10 11 -1 -1 -1 -1 12 13 -1 -1 -1 -1 -1 -1
#
#                               1
#                             /   \
#                           2       3
#                          / \     / \
#                         4   5   8   9
#                            / \     / \
#                           6   7   10  11
#                                  /  \
#                                 12  13
#
#    node = 7 , k = 3 -> ancestor 1
#    node = 7 , k = 2 -> ancestor 2
#    node = 12, k = 1 -> ancestor 10
#    node = 12, k = 5 -> ancestor -1


# ''' IMPORTANT CONCEPT REGARDING PYTHON, NESTED FUNCTION '''
# See below link to, learn how to use variable in nested functions
# and change their values
# 1. global variables   -> global
# 2. iterables  ->  x = [k]
# 3. nonlocal  -> nonlocal keyword
# 4. using function and dot . operator -> f1.x = k

#  https://www.geeksforgeeks.org/python-inner-functions/


# Time Complexity : O(n)
# Space complexity: O(1)

def kthAncestor(root, node, k):
    res = []

    # using iterables
    # x = [k]

    def find(root, node):
        nonlocal k

        if root is None:
            return False

        if root.data == node:
            k = k - 1
            # x[0] = x[0] - 1
            return True

        else:

            inLeftSubTree = find(root.left, node)
            if inLeftSubTree:
                if k == 0:
                    # if x[0] == 0:
                    res.append(root.data)
                    return False

                k = k - 1
                # x[0] = x[0] - 1
                return


            inRightSubTree = find(root.right, node)
            if inRightSubTree:
                if k == 0:
                    # if x[0] == 0:
                    res.append(root.data)
                    return False

                k = k - 1
                # x[0] = x[0] - 1
                return True

    find(root, node)
    return res if res else [-1]


BT = BinaryTreeInputPrint
# 1 2 3 4 5 8 9 -1 -1 6 7 -1 -1 10 11 -1 -1 -1 -1 12 13 -1 -1 -1 -1 -1 -1
root = BT.buildLevelTree()

testCases = [[7, 3],
             [7, 2],
             [12, 1],
             [12, 5]]

for node, k in testCases:
    ans = kthAncestor(root, node, k)
    print(f"{k} ancestor of {node} is {ans[0]} ")
