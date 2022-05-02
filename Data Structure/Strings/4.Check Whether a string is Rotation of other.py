# CONCEPT:
# s1 = ABCD , s2 = CDAB return -->true
# what we can do is to take a Temp string --> temp=''
# now we can do --> temp = s1 + s1 = ABCDCDAB
# Now using a built in function count() to check if s2 is present in temp


def checkRotation(s1, s2):
    # edge case:
    if len(s1) != len(s2):
        return "No"
    temp = s1 + s1
    # temp.count returns the number of occurrences of
    # the second string in temp
    if (temp.count(s2) > 0):
        return "YES"
    else:
        return "No"


s1 = input()
s2 = input()
print(checkRotation(s1, s2))
