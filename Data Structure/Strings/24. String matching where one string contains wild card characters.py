# * --> Matches with 0 or more instances of any character or set of characters.
# ? --> Matches with any one character.
# For example, “g*ks” matches with “geeks” match.
# And string “ge?ks*” matches with “geeksforgeeks”
# (note ‘*’ at the end of first string).
# But “g*k” doesn’t match with “gee” as character ‘k’ is not present in second string.


# test("g*ks", "geeks"); // Yes
# test("ge?ks*", "geeksforgeeks"); // Yes
# test("g*k", "gee"); // No because 'k' is not in second
# test("*pqrs", "pqrst"); // No because 't' is not in first
# test("abc*bcd", "abcdhghgbcd"); // Yes
# test("abc*c?d", "abcd"); // No because second must have 2 instances of 'c'
# test("*c*d", "abcd"); // Yes
# test("*?c*d", "abcd"); // Yes


def matching(str1, str2):
    # if both string are 0 length:
    if len(str1) == 0 and len(str2) == 0:
        return True

    # if str1[0] is '*' and str2 is 0 length --> false
    if len(str1) > 1 and str1[0] == '*' and len(str2) == 0:
        return False

    # first character of both matches or str1[0] is '?'
    if len(str1) > 1 and str1[0] == '?' \
            or len(str1) != 0 and len(str2) != 0 and str1[0] == str2[0]:
        return matching(str1[1:], str2[1:])

    # special case if str1[0] =='*' ,
    if len(str1) != 0 and str1[0] == '*':
        return matching(str1[1:], str2) or matching(str1, str2[1:])

    return False


str1 = input()
str2 = input()
print(str1, str2)
