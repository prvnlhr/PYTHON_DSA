import BinaryTreeInputPrint


# 1 4 4 6 9 5 -1 10 5 -1 -1 -1 -1 -1 -1 -1 -1
# 2 2 2 3 -1 3 -1 -1 -1 -1 -1


# This problem is based on serialization of binary tree
# We have to find duplicate subtree in binary tree.
# Now we want a way to check if a subtree is already encountered or not.
# so we can use serialization technique.
# Serialization means to convert a tree in form a string representation
# if we have serialize string representation of all node , we can easily solve this question
# for a particular node get its string representation and check if similar string is already,
# present in map of not,if yes then we have already encountered duplicate subtree
# we recursively traverse from left and right subtree to get their serialize strings
class Solution:
    def printAllDups(self, root):

        # result will store nodes of common subtree
        result_node_arr = []
        # map to store and check serialize string of subtree
        map = {}

        def helper(root):
            if root is None:
                return 'x'
            # traverse left and right subtree and get serialize string
            leftStr = helper(root.left)
            rightStr = helper(root.right)

            # Both below are correct, but since we want for just
            # checking in map we can use first format.
            # but if we want for deserialization purpose like(prblm 19.0)
            # we can use second format so that we can split on basis of ','

            # '^' this represents start of every node
            # if ^ is not there we will get wrong answer
            # consider this case:
            #          2
            #        /   \
            #      1      11
            #    /       /
            #  11       1
            # for left-subtree node(1) we get 111xxx
            # for right-subtree node(11) we get 111xxx
            # now 111xxx and 111xxx is same but the subtrees are diff for node 1 and 11
            # now if we use '^' we get,
            # ^1^11xxx and ^11^1xxx so both are diff and we correct answer
            # '^' this represents start of next node, which will give us correct result

            Str = '^' + str(root.data) + leftStr + rightStr
            # Str = str(root.data) + ',' + leftStr + ',' + rightStr

            # check if this string in present in map
            # if present then append this root to result array
            # else put this string in map

            if Str in map:
                map[Str] = map[Str] + 1
                # This condition is to prevent from,
                # same node appending again and again in result.
                if map[Str] == 2:
                    result_node_arr.append(root)
            else:
                map[Str] = 1
            return Str

        helper(root)
        print(map)
        for i in result_node_arr:
            print(i.data)
        return result_node_arr


BT = BinaryTreeInputPrint
root = BT.buildLevelTree()
ob = Solution()
ans = ob.printAllDups(root)
for node in ans:
    BT.PrintLevelWise(node)
