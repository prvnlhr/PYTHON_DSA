import BST


# LEETCODE
# SEE STRIVER'S YT VIDEO

class BSTIterator:

    def __init__(self, root):
        self.stack1 = []
        self.stack2 = []
        self.pushAllLeft(root)
        self.pushAllRight(root)

    def next(self):
        tempNode = self.stack1.pop()
        self.pushAllLeft(tempNode.right)
        return tempNode.data

    def before(self):
        if not self.stack2:
            return -1
        tempNode = self.stack2.pop()
        self.pushAllRight(tempNode.left)
        return tempNode.data

    def hasNext(self):
        return len(self.stack1) != 0

    def pushAllLeft(self, node):
        while node:
            self.stack1.append(node)
            node = node.left

    def pushAllRight(self, node):
        while node:
            self.stack2.append(node)
            node = node.right


# ______________________________________________________________________________________
#
#                  7
#                /   \
#               3     15
#                    /   \
#                   9    20
#
# 7 3  15 -1 -1 9 20 -1 -1 -1 -1

root = BST.buildLevelTree()
obj = BSTIterator(root)
print(obj.next())  # return 3
print(obj.next())  # return 7
print(obj.before())
print(obj.before())
# print(obj.hasNext())  # return True
# print(obj.next())  # return 9
# print(obj.hasNext())  # return True
# print(obj.next())  # return 15
# print(obj.hasNext())  # return True
# print(obj.next())  # return 20
# print(obj.hasNext())  # return False
