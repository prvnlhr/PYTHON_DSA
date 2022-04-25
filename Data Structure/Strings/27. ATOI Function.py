# APPROACH:
# To convert a string to integer we take each char of string.
# Now we find the ascii value of that char, using ord(char).
# Now to get get the integer value of that char,
# if we do ord(char) - ord('0') -> we get integer of char
# Now to handle diff below cases,
# 1. -12345 -> we can use sign var to decide if first char is '-' or not
# 2. abc23 -> if ord(char)-ord('0') is in range 0 -> 9 , then only we will have res


def atoiFunction(str):
    res = 0
    sign = 1

    if str[0] == '-':
        sign = -1

    for char in str:
        newVal = ord(char) - ord('0')

        if newVal <= 9 and newVal >= 0:
            oldVal = res * 10
            res = oldVal + newVal
    return res * sign


testCases = ['abc23', '12439', '-12345','00-42', '+-42','  45']
for str in testCases:
    ans = atoiFunction(str)
    print(ans)
    print()
