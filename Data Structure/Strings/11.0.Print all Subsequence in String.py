# Ex_ abcd

# 'abcd'
# 'abc'
# 'abd'
# 'ab'
# 'acd'
# 'ac'
# 'ad'
# 'a'
# 'bcd'
# 'bc'
# 'bd'
# 'b'
# 'cd'
# 'd'
# 'c'


# PICK AND DON'T PICK
def getAllSubsequences(s):
    res = []

    def getAll(s, output):
        if len(s) == 0:
            res.append(output)
            return

        getAll(s[1:], output + s[0])
        getAll(s[1:], output)

    getAll(s, '')
    return res


s = input()
ans = getAllSubsequences(s)
print(ans)
