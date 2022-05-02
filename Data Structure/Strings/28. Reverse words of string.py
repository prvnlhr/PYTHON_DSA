# Ex_1.
# Welcome   to Coding Ninjas
# Ninjas Coding to Welcome


# Ex_2.
#    I am   a    star
# star a am I

# Ex_3.
# Hello  World!!
# World!! Hello


def rev(s):
    res = ''
    arr = s.split(' ')
    n = len(arr)
    j = n - 1
    while j >= 0:
        char = arr[j]
        if char != "":
            res += char + ' '
        j -= 1
    return res[0:len(res) - 1]


# CN --> O(N)
def reverseAllWords(s):
    res = ''
    n = len(s)
    start = n - 1

    while start >= 0:

        if s[start] == ' ':
            start -= 1
        # get reverse of word
        else:
            j = start
            while j >= 0 and s[j] != ' ':
                j -= 1
            if len(res) > 0:
                res += ' '
            res += s[j + 1:start + 1]
            start = j
    return res


def reverseWords(s):
    arr = list(s)
    reverse_string(arr, 0, len(arr) - 1)
    reverse_word(arr)
    word = trim_sides(arr)
    res = trim_space(word)
    return ''.join(res)


def reverse_string(arr, l, r):
    '''reverse a given string'''
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


def reverse_word(arr):
    '''reverse every words in a string'''
    l, r = 0, 0
    while r < len(arr):
        while r < len(arr) and not arr[r].isspace():
            r += 1
        reverse_string(arr, l, r - 1)
        r += 1
        l = r
    return arr


def trim_sides(arr):
    '''str.strip() basically'''
    if ''.join(arr).isspace(): return []
    l, r = 0, len(arr) - 1
    while l < r and arr[l].isspace(): l += 1
    while l < r and arr[r].isspace(): r -= 1
    return arr[l:r + 1]


def trim_space(word):
    '''remove duplicating space in a word'''
    if not word: return []
    res = [word[0]]
    for i in range(1, len(word)):
        if res[-1].isspace() and word[i].isspace(): continue
        res.append(word[i])
    return res


# str = '    I am   a    star'
str = 'Welcome   to Coding Ninjas'

ans = reverseStringWords(str)
print(ans)
