import BinaryTreeInputPrint


class Solution:

    def checkSubTree(self, root):
        map = {}

        def solve(root):
            # if root is None
            if root is None:
                return "$"

            # root left and right both are None
            if not root.left and not root.right:
                return str(root.data)

            s = ""
            s += str(root.data)
            s += solve(root.left)
            s += solve(root.right)

            if s not in map:
                map[s] = 1
            else:
                map[s] += 1
            return s

        solve(root)
        for key in map:
            if map[key] > 1:
                return 'Yes'
        return 'No'


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()

ob = Solution()
ans = ob.checkSubTree(root)
print(ans)
