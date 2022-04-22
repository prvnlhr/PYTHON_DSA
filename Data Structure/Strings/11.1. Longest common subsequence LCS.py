result = []


def lcsHelper(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        result.append(s1[i])
        ans = 1 + lcsHelper(s1, s2, i + 1, j + 1)

    else:
        a = lcsHelper(s1, s2, i, j + 1)
        b = lcsHelper(s1, s2, i + 1, j)
        ans = max(a, b)
    return ans


def lcs(s1, s2):
    return lcsHelper(s1, s2, 0, 0)


s1 = input()
s2 = input()
print(lcs(s1, s2))
print(result)
