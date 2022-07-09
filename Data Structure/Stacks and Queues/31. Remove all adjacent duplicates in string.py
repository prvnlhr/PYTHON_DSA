# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb"
# since the letters are adjacent and equal, and
# this is the only possible move.  The result of this
# move is that the string is "aaca", of which only "aa"
# is possible, so the final string is "ca".

# Example 2:
# Input: s = "azxxzy"
# Output: "ay"

def removeDuplicates(Str):
    stack = []
    stack.append(Str[0])
    curr_index = 1
    while curr_index < len(Str):
        element = Str[curr_index]
        if stack and stack[-1] == element:
            stack.pop()
        else:
            stack.append(element)
        curr_index = curr_index + 1

    return ''.join(stack)
