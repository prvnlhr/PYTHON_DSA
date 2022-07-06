# Input: s = "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

def removeOuterParentheses(S):
    res = []
    open_brackets = 0
    for char in S:
        if char == '(' and open_brackets > 0:
            res.append(char)
        if char == ')' and open_brackets > 1:
            res.append(char)

        if char == '(':
            open_brackets += 1
        else:
            open_brackets -= 1
    return ''.join(res)


def removeOuterParentheses1(S):
    cnt = 0
    res = ''
    for c in S:

        # close ____________
        if c == ')':
            cnt -= 1

        # count != 0 _______
        if cnt != 0:
            res += c

        # open _____________
        if c == '(':
            cnt += 1

    return res


s = input()
print(removeOuterParentheses(s))
