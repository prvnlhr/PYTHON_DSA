# LEETCODE
# THIS SOLUTION SEEMS CORRECT BUT gets TLE
def KthAncestor(parent, node, k):
    curr_node = node
    while k > 0:
        if k > 0 and curr_node == -1:
            return -1
        curr_node_parent = parent[curr_node]
        curr_node = curr_node_parent
        k = k - 1
    return curr_node_parent


parent = [int(i) for i in input().strip().split()]
ans = KthAncestor(parent, 3, 5)
print(ans)
ans = KthAncestor(parent, 3, 2)
print(ans)
ans = KthAncestor(parent, 2, 2)
print(ans)
ans = KthAncestor(parent, 0, 2)
print(ans)
ans = KthAncestor(parent, 2, 1)
print(ans)
