# You are given a parentheses string s. In one move,
# you can insert a parenthesis at any position of the string.
#
# For example, if s = "()))", you can insert an opening parenthesis
# to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Input: str = "())"
# Output: 1
# One '(' is required at beginning.
#
# Input: str = "((("
# Output: 3
# Three ')' is required at end.
from collections import deque


# IN BOTH THE BELOW SOLUTIONS, THE LOGIC IS SAME
# now according to prblm, we have to find how many open or
# close brackets we need to add to make string valid
# So the basic intuition is as follows,
# while traversing the string ,if we find a valid pair, we will remove
# it and move further, so at end only char which are not valid will be remaining
# and by counting no of open and closed from remaining we can find our ans.
# SO now the problem boils down to removing all valid pair and keeping only invalid.
# We can use a stack, and put open brackets in stack and if we found a
# for a closing bracket in stack match we remove it,so at end
# in stack only invalid brackets will be remaining ,which will give our ans.
# Now , to further to optimised space, and to avoid using stack ,we
# can use count of open and closed brackets,to match a pair.


# INTUITION::
# We will maintain open ,close brackets count.
# if char =='(' i.e. open increase open _count
# if char == ')' i.e close increase close _count
# but there is a catch, if char is closing ')' and we have a open bracket _count
# greater then 1, then we can formed a pair, so we will, decrease then open_count,
# rather then increasing close_count, else if, if we don't have open_count,
# then simply we will increase close_count.
# at end our ans will be open_count + close_count

# O(N),O(N)
def insert1(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)

    return len(stack)


# O(N),O(1)
def insert(s):
    close_count = 0
    open_count = 0
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count >= 1:
                open_count -= 1
            else:
                close_count += 1
    return close_count + open_count


testCases = ['()))', '())', '(((', '()', '()))((', ')()', ')(', '(()(']
for test in testCases:
    ans = insert(test)
    print(test, "--> ", ans)
