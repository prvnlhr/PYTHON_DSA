def checkPalindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return 'No'
        i = i + 1
        j = j - 1
    return 'YES'


s = input()
isPalindrome = checkPalindrome(s)
print(isPalindrome)
