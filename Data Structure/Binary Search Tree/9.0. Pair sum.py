import BST


# _CN_________________________________________________________________________________

def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)


def printNodesSumToS1(root, s):
    if root == None:
        return
    totalNodes = countNodes(root)
    count = 0
    inorder = []
    revInorder = []
    temp = root
    while temp != None:
        inorder.append(temp)
        temp = temp.left
    temp = root
    while temp != None:
        revInorder.append(temp)
        temp = temp.right
    # for i in range(len(inorder)):
    #     print(inorder[i].data, end=" ")
    #     print()
    # for i in range(len(revInorder)):
    #     print(revInorder[i].data, end=" ")
    #     print()

    while count < totalNodes - 1:
        top1 = inorder.pop()
        top2 = revInorder.pop()
        inorder.append(top1)
        revInorder.append(top2)
        if top1.data + top2.data == s:
            top = top1
            inorder.pop()
            count = count + 1
            if top.right != None:
                top = top.right
                while top != None:
                    inorder.append(top)
                    top = top.left
            top = top2
            revInorder.pop()
            count = count + 1
            if top.left != None:
                top = top.left
                while top != None:
                    revInorder.append(top)
                    top = top.right
        elif top1.data + top2.data > s:
            top = top2
            revInorder.pop()
            count = count + 1
            if top.left != None:
                top = top.left
                while top != None:
                    revInorder.append(top)
                    top = top.right
        else:
            top = top1
            inorder.pop()
            count = count + 1
            if top.right != None:
                top = top.right
                while top != None:
                    inorder.append(top)
                    top = top.left


# LEETCODE O(H) solution
# class Solution:
#     def findTarget(self, root, k):
#         def inOrder(root):
#             if root:
#                 yield from inOrder(root.left)
#                 yield root.val
#                 yield from inOrder(root.right)
#
#         def inOrderReversed(root):
#             if root:
#                 yield from inOrderReversed(root.right)
#                 yield root.val
#                 yield from inOrderReversed(root.left)
#
#         leftGenerator = inOrder(root)
#         rightGenerator = inOrderReversed(root)
#
#         left, right = next(leftGenerator), next(rightGenerator)
#         while left < right:
#             if left + right == k: return True
#             if left + right < k:
#                 left = next(leftGenerator)
#             else:
#                 right = next(rightGenerator)
#         return False


# O(N) O(H)*2
# SEE STRIVER'S YT VIDEO
# BST ITERATOR SOLUTION
# BEST
class Solution:
    def findTarget(self, root, k):

        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        # 1.
        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        # 2.
        left, right = nextLeft(stLeft), nextRight(stRight)

        while left < right:
            if left + right == k:
                return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False


# O(N), O(N)
def pairSum(root, sum):
    res = []
    map = set()

    def findPair(root):
        if root is None:
            return []
        if sum - root.data in map:
            res.append((sum - root.data, root.data))
            return True
        map.add(root.data)
        left = findPair(root.left)
        right = findPair(root.right)
        return left or right

    return findPair(root)
    # return res


# ___GeeksForGeeks 100% correct___________________________________________________________________
def printNodesSumToS2(root, s):
    d = set()
    sum = s
    findPair(root, sum, d)


def findPair(root, sum, set):
    # base case
    if root is None:
        return False

    # return true if pair is found in the left subtree else continue
    # processing the node
    if findPair(root.left, sum, set):
        return True

    # if pair is formed with current node, print the pair and return True
    if sum - root.data in set:
        print(sum - root.data, root.data)
        return True

    # insert current node's value into the set
    else:
        set.add(root.data)
    # search in right subtree
    return findPair(root.right, sum, set)


# _________________________________________________________________________________________

# Main
root = BST.buildLevelTree()
s = int(input())
# printNodesSumToS1(root, s)
ans = pairSum(root, s)
print(ans)
# printNodesSumToS2(root, s)
