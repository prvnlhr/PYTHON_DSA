from collections import defaultdict


# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2


# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0


# O(N), O(N)
def strStr1(haystack, needle):
    map = defaultdict(list)
    m = len(haystack)
    n = len(needle)

    res = -1
    for i in range(m - n + 1):
        start = i
        end = i + n
        s = haystack[i:end]
        print(s)
        print(map)
        if s not in map:
            map[s] = [i]
        elif s in map:
            map[s].append(i)
    return map[needle][0]


# O(N) , O(1)
def strStr(haystack, needle):
    m = len(haystack)
    n = len(needle)
    for i in range(len(haystack) - len(needle) + 1):
        start = i
        end = i + n
        s = haystack[start:end]
        if s == needle:
            return i
    return -1


haystack = "hellomynameisPraveen"
needle = "Pra"
ans = strStr(haystack, needle)
print(ans)
