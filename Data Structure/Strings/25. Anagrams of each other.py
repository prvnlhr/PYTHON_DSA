def areAnagram(str1, str2):
    if len(str1) != len(str2):
        return 0

    ordVal1 = 0
    ordVal2 = 0
    for char1, char2 in zip(str1, str2):
        ordVal1 += ord(char1)
        ordVal2 += ord(char2)
    if ordVal1 == ordVal2:
        return 1
    return 0


str1 = 'listen'
str2 = 'silent'
areAnagram(str1, str2)
