import BST
import sys


# SOL 2._________________________________

class Solution:

    # This Solution seems complex but it is easy,
    # INTUITION::
    # we have  MIN and MAX values,
    # if root lies between MIN AND MAX then its ok
    # but if root is out of the MIN and MAX range,  smaller then MIN }---MIN<-[root]->MAX---{ greater then MAX
    # then isBST is False
    # now for every left-subtree what is MAX value ?, the ans is, root itself is MAX for leftSubtree
    # for every right subtree, root is MIN
    # therefore, recurring left side 'root-1' becomes MAX and for right side 'root+1' becomes MIN
    def isBST(self, root):

        def isBSTHelper(root, MIN, MAX):
            if root is None:
                return True

            if root.data < MIN or root.data > MAX:
                return False

            return isBSTHelper(root.left, MIN, root.data - 1) and isBSTHelper(root.right, root.data + 1, MAX)

        return isBSTHelper(root, float('-inf'), float('inf'))


#
# # SOL 1._________________________________
# class isBSTReturn:
#     def __init__(self, min, max, isBST):
#         self.min = min
#         self.max = max
#         self.isBST = isBST
#
#
# # O(n) worst case
# def isBST(root):
#     if root is None:
#         return isBSTReturn(sys.maxsize, ~sys.maxsize, True)

#     # 1. finding leftAns and rightAns
#     leftAns = isBST(root.left)
#     rightAns = isBST(root.right)
#
#     # 2. Assigning Min and Max
#     Min = min(root.data, min(leftAns.min, rightAns.min))
#     Max = max(root.data, max(leftAns.max, rightAns.max))
#
#     # variable for current ans
#     isBst = True
#     # 3. Checking from ans
#     if leftAns.max >= root.data:
#         isBst = False
#     # checking if left isBSt
#     if leftAns.isBST == False:
#         isBst = False
#     # checking if right isBSt
#     if rightAns.isBST == False:
#         isBst = False
#
#     # 4. returning ans concluded
#     ans = isBSTReturn(Min, Max, isBst)
#     return ans


root = BST.buildLevelTree()
# ans = isBST(root)
obj = Solution()
ans1 = obj.isBST(root)
print(ans1)
