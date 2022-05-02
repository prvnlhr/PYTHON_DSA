# Optimised O(n^2): can be further optimised.
def printAllSubs(s):
    res = []
    for i in range(len(s)):
        subStr = ''
        for j in range(i, len(s)):
            subStr += s[j]
            res.append(subStr)
    return res


s = 'abcd'
print(printAllSubs(s))
