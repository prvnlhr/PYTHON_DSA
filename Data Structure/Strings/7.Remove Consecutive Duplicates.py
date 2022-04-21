# aabccba
# abcba
# xxxyyyzwwzzz
# xyzwz


def removeConsecutiveDuplicates(string):
    string = string + ' '
    newStr = ''
    start = string[0]
    for j in range(len(string)):
        if (string[j] != start):
            newStr = newStr + start
            # print(newStr)
            start = string[j]
    return newStr


# Recursive CN:
def removeConsecutiveDuplicates(string):
    if len(string) <= 1:
        return string
    string2 = removeConsecutiveDuplicates(string[1:])
    if string[0] == string[1]:
        return string2
    else:
        return string[0] + string2


string = input()
ans = removeConsecutiveDuplicates(string)
print(ans)
