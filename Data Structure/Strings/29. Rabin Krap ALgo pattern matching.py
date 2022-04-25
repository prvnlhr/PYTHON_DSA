from collections import defaultdict

d = 10


def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m - 1):
        h = (h * d) % q
    print(h)

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    print(p, t)

    # Find the match
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("Pattern is found at position: " + str(i + 1))

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t = t + q


# GFG_____________________________________________________________
# Given two strings, one is a text string and other is a
# pattern string. The task is to print the indexes of all
# the occurrences of pattern string in the text string. For
# printing, Starting Index of a string should be taken as 1.
#
# Example 1:
#
# Input:
# S = "batmanandrobinarebat", pat = "bat"
# Output: 1 18
# Explanation: The string "bat" occurs twice
# in S, one starts are index 1 and the other
# at index 18.
# â€‹Example 2:
#
# Input:
# S = "abesdu", pat = "edu"
# Output: -1
# Explanation: There's not substring "edu"
# present in S.
#
# Your Task:
# You don't need to read input or print anything.
# Your task is to complete the function search() which
# takes the string S and the string pat as inputs and
# returns an array denoting the start indices (1-based)
# of substring pat in the string S.

# This is self solved 100% correct map based code
# O(N), O(N)
# BUT TO SOLVE THIS PROBLEM THERE ARE FOLLOWING ALGO
# RABIN KARP
# KMP ALGO
# Z ALGO

def searchMap(pattern, text):
    map = defaultdict(list)
    m = len(text)
    n = len(pattern)
    for i in range(m - n + 1):
        start = i
        end = i + n
        s = text[start:end]
        if s not in map:
            map[s] = [i + 1]
        elif s in map:
            arr = map[s]
            arr.append(i + 1)

    if len(map[pattern]) != 0:
        return map[pattern]
    else:
        return [-1]


text = "cxggbw"
pattern = "n"
q = 13
ans = searchMap(pattern, text)
print(ans)
# search(pattern, text, q)
