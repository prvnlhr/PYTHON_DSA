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


# Welcome   to Coding Ninjas
# Ninjas Coding to Welcome


# Ex_2.
#    I am   a    star
# star a am I

# s = '    I am   a    star'
# s = 'Welcome   to Coding Ninjas'
# s = 'Welcome   to Coding Ninjas   '
s = ' '
# s = '   Welcome   to Coding Ninjas   '
ans = reverseAllWords(s)
print(ans, len(ans))
