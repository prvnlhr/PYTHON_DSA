# O(n) and O(n) stack sol:
# Input: str = "(()()"
#
# Initialize result as 0 and stack with one item -1.
#
# For i = 0, str[0] = '(', we push 0 in stack
#
# For i = 1, str[1] = '(', we push 1 in stack
#
# For i = 2, str[2] = ')', currently stack has
# [-1, 0, 1], we pop from the stack and the stack
# now is [-1, 0] and length of current valid substring
# becomes 2 (we get this 2 by subtracting stack top from
# current index).
#
# Since the current length is more than the current result,
# we update the result.
#
# For i = 3, str[3] = '(', we push again, stack is [-1, 0, 3].
# For i = 4, str[4] = ')', we pop from the stack, stack
# becomes [-1, 0] and length of current valid substring
# becomes 4 (we get this 4 by subtracting stack top from
# current index).
# Since current length is more than current result,
# we update result.

def findLength(s):
    stack = []
    stack.append(-1)
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)

        else:
            if len(stack) != 0:
                stack.pop()
            if len(stack) != 0:
                result = max(result, i - stack[-1])
            else:
                stack.append(i)
    return result


# _____________________________________________________________________________________
# O(n) and O(1) Easy Sol
def findLength(s):
    left = right = 0
    maxLength = 0
    #
    #
    # traversing form left-->right
    for i in range(len(s)):

        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            maxLength = max(maxLength, 2 * right)
        elif right > left:
            left = right = 0
    #
    #
    # traversing from right-->left
    left = right = 0
    for i in range(len(s) - 1, -1, -1):

        if s[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            maxLength = max(maxLength, 2 * left)
        elif left > right:
            left = right = 0
    #
    #
    #
    return maxLength


s = input()
print(findLength(s))
