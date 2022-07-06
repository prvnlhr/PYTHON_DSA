#
# Input : ((()
# Output : 2
# Explanation : ()
#
# Input: )()())
# Output : 4
# Explanation: ()()
#
# Input:  ()(()))))
# Output: 6
# Explanation:  ()(())
#
#
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

# Input : ((() --> 2
# Input: )()()) --> 4
# Input:  ()(())))) --> 6
#
# In above all examples, one thing that is common
# is that length of valid substring, will be the number
# of pairs of open-close brackets
# In ex 1 -> () only one pair so length == 2
# In ex 2 -> () () two pairs so length == 4
# In ex 3 -> () () () three pairs so length == 6
#
# So what we are basically doing is calculating open and closed brackets
# and if open and closed brackets become equal we have pair, which will be equal
# This logic is used below.
# So we will calculate open and closed brackets form left and right,
# and if any point they become equal, that means the number of pairs
# is equal to their count
#


def findLength(s):
    open_brackets = close_brackets = 0
    maxLength = 0
    #
    #
    # __traversing form open_brackets --> close_brackets
    for i in range(len(s)):

        if s[i] == '(':
            open_brackets += 1
        else:
            close_brackets += 1
        # if open_brackets == close_brackets we have a pair,so length of pair will be 2* pair count
        # and pair count is close_brackets
        if open_brackets == close_brackets:
            maxLength = max(maxLength, 2 * close_brackets)
        # if close_brackets is more means, then we have no pair so open_brackets==close_brackets ==0
        elif close_brackets > open_brackets:
            open_brackets = close_brackets = 0
    #
    # SIMILARLY___right --> open_brackets
    # __traversing from close_brackets --> open_brackets
    open_brackets = close_brackets = 0
    for i in range(len(s) - 1, -1, -1):

        if s[i] == '(':
            open_brackets += 1
        else:
            close_brackets += 1

        if open_brackets == close_brackets:
            maxLength = max(maxLength, 2 * open_brackets)
        elif open_brackets > close_brackets:
            open_brackets = close_brackets = 0
    #
    #
    #
    return maxLength


s = input()
print(findLength(s))
