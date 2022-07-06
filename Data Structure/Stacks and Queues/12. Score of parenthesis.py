# Given a balanced parentheses string s, return the score of the string.
#
# The score of a balanced parentheses string is based on the following rule:
#
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Example 1:
# Input: s = "()"
# Output: 1
#
# Example 2:
# Input: s = "(())"
# Output: 2

def scoreOfParentheses(S):
    stack = [0]

    for par in S:
        print(stack)

        if par == "(":
            stack.append(0)

        elif par == ')':
            previous_score = stack.pop()

            if previous_score == 0:
                new_score = 1
            else:
                new_score = previous_score * 2

            stack[-1] += new_score

    return stack[0]


def scoreOfParentheses1(S):
    stack = [0]
    for par in S:
        print(par)
        print("b", stack)
        if par == "(":
            stack.append(0)
        else:
            last = stack.pop()
            if last == 0:
                score = 1
            else:
                score = last * 2
            stack[-1] += score
        print("a", stack)
        print()

    return stack[0]


# s = '()()((()))'
s ='()()'
ans = scoreOfParentheses1(s)
print(ans)
