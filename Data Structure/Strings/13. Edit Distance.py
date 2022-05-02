def editDistanceHepler(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if s1[m] == s2[n]:
        return editDistanceHepler(s1, s2, m - 1, n - 1)

    a = editDistanceHepler(s1, s2, m - 1, n)
    b = editDistanceHepler(s1, s2, m, n - 1)
    c = editDistanceHepler(s1, s2, m - 2, n - 1)
    return 1 + min(a, b, c)


def editDistance(s1, s2):
    editDistanceHepler(s1, s2, len(s1), len(s2))
