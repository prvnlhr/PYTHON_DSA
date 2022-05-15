import queue

import BinaryTreeInputPrint


class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# NOTE:
# First iterative solution stores serialize String in format,
# 1,2,3,4,5,6,7,#,#,#,#,#,#,#,#
# whereas, second recursive approach stores it like,
# 1,2,4,x,x,5,x,x,3,6,x,x,7,x,x
#
# As we can see first type is more efficient space wise, because it stores
# less leading '#' as compare to 'x'


# __Iterative BFS solution___
# O(N) and O(N)

# Level Order serialization
def serializaBt(root):
    if not root:
        return ''
    q = queue.Queue()
    q.put(root)
    ans = []

    while not q.empty():
        node = q.get()
        if node:
            q.put(node.left)
            q.put(node.right)

        if node:
            ans.append(str(node.data))
        else:
            ans.append('#')
    return ','.join(ans)


# Level Order deserialization
def deserializeBt(serializeString):
    if not serializeString:
        return None
    input = serializeString.split(',')
    index = 0

    root = BTNode(int(input[index]))
    index = 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if input[index] != '#':
            node.left = BTNode(int(input[index]))
            q.put(node.left)
        index = index + 1
        if input[index] != '#':
            node.right = BTNode(int(input[index]))
            q.put(node.right)
        index = index + 1
    return root


# __Recursive Approach_______________________________________________________________________
def deserializeBTRec(serializeStr):
    arr = serializeStr.split(',')

    def deserializeHelper():
        node_next = arr.pop(0)
        if node_next == 'x':
            return None
        newNode = BT.BinaryTreeNode(int(node_next))
        newNode.left = deserializeHelper()
        newNode.right = deserializeHelper()
        return newNode

    newRoot = deserializeHelper()
    # print BT
    BT.PrintLevelWise(newRoot)


# Basically it is PREORDER serialization
def serializeBtRec(root):
    if root is None:
        return 'x'
    leftStr = serializeBtRec(root.left)
    rightStr = serializeBtRec(root.right)
    return str(root.data) + ',' + leftStr + ',' + rightStr


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
serializeStr = serializeBtRec(root)
print(serializeStr)
deserializeBTRec(serializeStr)
print()
ans = serializaBt(root)
print(ans)
newroot = deserializeBt(ans)
BT.PrintLevelWise(newroot)
