import BinaryTreeInputPrint


class Solution:
    # O(m + n)
    # m --> num of node of root1 and n--> num of nodes of root2
    def checkSubtreeOrNot(self, root1, root2):
        def getString(root):
            if not root:
                return '#'
            else:
                # '^' -> is important for Ex_1. test case
                # if we don't use it,
                # s1 -> 12##
                # s2 -> 2##
                # this make s2 substring of s1 ,as 2## is present in s1
                # but if use '^', we get,
                # s1 -> ^12##
                # s2 -> ^2##
                # thus s2 is not substring of s1
                return '^' + str(root.data) + getString(root.left) + getString(root.right)

        s1 = getString(root1)
        print(s1)
        s2 = getString(root2)
        print(s2)
        ans = s2 in s1  # check if subString
        return ans


# Ex_1
# 3 4 5 1 2 -1 -1 -1 -1 0 -1 -1 -1
# 4 1 2 -1 -1 -1 -1
# Ex_2
# 1 2 -1 -1 -1
# 2 -1 -1
BT = BinaryTreeInputPrint
root1 = BT.buildLevelTree()
root2 = BT.buildLevelTree()
ob = Solution()
ans = ob.checkSubtreeOrNot(root1, root2)
print(ans)
