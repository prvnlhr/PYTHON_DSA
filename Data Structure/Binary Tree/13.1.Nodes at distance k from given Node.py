import BinaryTreeInputPrint


#
# def nodesAtDistanceK(root, k, dist, result):
#     if root is None:
#         return
#     elif k == 0:
#         print(root.data)
#         result.append(root.data)
#
#     nodesAtDistanceK(root.left, k, dist + 1, result)
#     nodesAtDistanceK(root.right, k, dist + 1, result)
#
#
# def distanceK(root, target, K):
#     ans = []
#
#     def dfs(node):
#         if not node:
#             return -1
#         elif node is target:
#             subtree_add(node, 0)
#             return 1
#         else:
#             L, R = dfs(node.left), dfs(node.right)
#             if L != -1:
#                 if L == K: ans.append(node.val)
#                 subtree_add(node.right, L + 1)
#                 return L + 1
#             elif R != -1:
#                 if R == K: ans.append(node.val)
#                 subtree_add(node.left, R + 1)
#                 return R + 1
#             else:
#                 return -1
#
#     # Add all nodes 'K - dist' from the node to answer.
#     def subtree_add(node, dist):
#         if not node:
#             return
#         elif dist == K:
#             ans.append(node.val)
#         else:
#             subtree_add(node.left, dist + 1)
#             subtree_add(node.right, dist + 1)
#
#     dfs(root)
#     print(ans)
#     return ans


#
# def nodes_at_K_dist_from_Node(root, target, k):
#     result = []
#
#     def nodesAtDistanceK(root, dist):
#         if root is None:
#             return
#         elif dist == 0:
#             result.append(root.data)
#         nodesAtDistanceK(root.left, dist + 1)
#         nodesAtDistanceK(root.right, dist + 1)
#
#     def recursiveDFS(root):
#
#         if root is None:
#             return -1
#
#         elif root.data == target:
#             nodesAtDistanceK(root, 0)
#             return 1
#         else:
#             L = recursiveDFS(root.left)
#             R = recursiveDFS(root.right)
#
#             if L != -1:
#                 if L == k:
#                     result.append(root.data)
#                 nodesAtDistanceK(root.right, L + 1)
#                 return L + 1
#
#             elif R != -1:
#                 if R == k:
#                     result.append(root.data)
#                 nodesAtDistanceK(root.left, R + 1)
#                 return R + 1
#             else:
#                 return -1
#
#     recursiveDFS(root)
#     return result


class Solution(object):
    def distanceK(self, root, target, K):
        print('1')
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if node == None:
                return False
            elif node == target:
                subtree_add(node, K)
                return True
            else:
                L = dfs(node.left)
                R = dfs(node.right)
                if L:
                    if L == K:
                        ans.append(node.data)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K:
                        ans.append(node.data)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.data)
                # print(ans)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)

        return ans


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
target = int(input())
k = int(input())
obj = Solution()
ans1 = obj.distanceK(root, target, k)
print(ans1)
