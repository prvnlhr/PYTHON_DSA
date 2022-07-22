new = ""
i = 0


def pairStar(s):
    global i
    l = len(s)
    if l == 1:
        return s
    if s[0] == s[1]:
        global new
        new = new + s[0] + "*"
        pairStar(s[1:])
    else:
        new = new + s[0]
        pairStar(s[1:])
    return new + s[l - 1]


s = input()
res = pairStar(s)
print(res)
