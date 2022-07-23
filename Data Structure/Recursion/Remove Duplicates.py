res =""
def removeConsecutiveDuplicates(string):
    l = len(string)
    global res
    if l==1:
        return string
    if string[0]==string[1]:
        removeConsecutiveDuplicates(string[1:])
    else:
        res = res + string[0]
        removeConsecutiveDuplicates(string[1:])
    return res + string[l]





string = input().strip()
print(removeConsecutiveDuplicates(string))
