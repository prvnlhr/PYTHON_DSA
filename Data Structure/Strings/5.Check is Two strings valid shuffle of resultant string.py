# example:
# 1XY2 is a valid shuffle of XY and 12
# Y12X is not a valid shuffle of XY and 12
# In the above example, we have a string array named results.
# It contains two strings: 1XY2 and Y12X.
# We are checking if these two strings are valid shuffle of strings first(XY) and second(12).
# Here, the program  1XY2 is a valid shuffle of XY and 12.
# However, Y12X is not a valid shuffle.
# This is because Y12X has altered the order of string XY.
# Here, Y is used before X.
# Hence, to be a valid shuffle, the order of string should be maintained.
# https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings

def shuffle(s1, s2, result):
    if len(result) != len(s1) + len(s2):
        return False

    i, j, k = 0, 0, 0
    while k < len(result):
        print(k, i, j)
        if (i < len(s1) and s1[i] == result[k]):
            i = i + 1
        if (j < len(s2) and s2[j] == result[k]):
            j = j + 1
        k = k + 1

    if i < len(s1) or j < len(s2):
        return False
    else:
        return True


s1 = input()
s2 = input()
result = input()
ans = shuffle(s1, s2, result)
print(ans)
