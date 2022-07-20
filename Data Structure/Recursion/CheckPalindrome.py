# solution 2
def checkPalindrome(s):
    return s == s[::-1]
#------------------------
# solution 1
def palindrome(s):
    l = len(s)
    if l <= 1:
        return True
    if s[0] != s[l - 1]:
        return False
    return palindrome(s[1:-1])

s = input()
l = len(s) - 1
#---------------------------
ans = (checkPalindrome(s))
if ans:
    print("true")
else:
    print("false")
#--------------------------
res = palindrome(s)
if palindrome(s):
    print("true")
else:
    print("false")




