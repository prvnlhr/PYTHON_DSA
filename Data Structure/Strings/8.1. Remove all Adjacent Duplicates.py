# Input: azxxzy
# Output: ay
# First “azxxzy” is reduced to “azzy”.
# The string “azzy” contains duplicates,so it is further reduced to “ay”.
# Input: geeksforgeeg
# Output: gksfor
# First “geeksforgeeg” is reduced to “gksforgg”. The string “gksforgg”
# contains duplicates, so it is further reduced to “gksfor”.
# Input: caaabbbaacdddd
# Output: Empty String
# Input: acaaabbbacdddd
# Output: acac

# Naive Solution will be to use nested Loops: very Bad Solution


# Better solution:Using STACK

def removeAllAdjacentDuplicates(string):
    stack = []
    i = 0
    while i < len(string):
        if len(stack) == 0 or stack[-1] != string[i]:
            stack.append(string[i])
            i = i + 1
        else:
            stack.pop()
            i = i + 1
    return stack


string = input()
# ans = removeAllAdjacentDuplicates(string)
ans = remove(string)
print(ans)
