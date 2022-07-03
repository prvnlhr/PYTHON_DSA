import BST


# Given a BST and an integer k. Find and return the path
# from the node with data k and root (if a node with data k
# is present in given BST) in a list. Return empty list otherwise.
# Note: Assume that BST contains all unique elements.

# Sample Input 1:
# 8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
# node = 2
# Sample Output 1:
# 2 5 8

# Self solved updated 100%
def rootToNodePath(root, node):
    res = []

    def findPath(root, node, path):
        if root is None:
            return []
        path = path + str(root.data)
        if root.data == node:
            return res.append(path)
        path = path + ' '
        if node < root.data:
            findPath(root.left, node, path)
        elif node > root.data:
            findPath(root.right, node, path)

    findPath(root, node, '')
    return res


result = []


def findPath1(root, node):
    if root is None:
        return None
    # if root == node
    # create a path array and append root
    if root.data == node:
        path = []
        path.append(root.data)
        return path
    # if root > node,then find path in left subtree
    # if path found is and is not none
    # append it to path array an d return
    elif node < root.data:
        path = findPath1(root.left, node)
        if path is not None:
            path.append(root.data)
        return path
    # if root < node ,  then find path in right subtree
    # if path is found and is not none
    # append it to path array an d return
    else:
        path = findPath1(root.right, node)
        if path is not None:
            path.append(root.data)
        return path


root = BST.buildLevelTree()
node = int(input())
ans = rootToNodePath(root, node)
print(ans)
