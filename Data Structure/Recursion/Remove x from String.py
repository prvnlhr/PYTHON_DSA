def removeX(string):
    l = len(string)
    if l==0:
        return string

    res =""

    if string[0]!='x':
        res = res + string[0]
    ans = removeX(string[1:])
    return res + ans








# Main
string = input()
print(removeX(string))



