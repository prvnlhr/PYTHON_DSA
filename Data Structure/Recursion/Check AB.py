
def checkab(str):
    if (len(str) == 0):
        return True
    if (str[0] == 'a'):
        if (len(str[1:]) > 1 and str[1:3] == 'bb'):
            return checkab(str[3:])
        else:
            return checkab(str[1:])
    else:
        return False


str = input()

if (checkab(str)):
    print("true")
else:
    print("false")
