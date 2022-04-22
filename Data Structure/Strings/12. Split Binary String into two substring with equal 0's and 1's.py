# Given a binary string str of length N, the task is to find the
# maximum count of consecutive substrings str can be divided into
# such that all the substrings are balanced i.e. they have equal
# number of 0s and 1s. If it is not possible to split str satisfying
# the conditions then print -1.

# Input: str = “0100110101”
# Output: 4
# The required substrings are “01”, “0011”, “01” and “01”.
#
# Input: str = “0111100010”
# Output: 3
#
# Input: str = “0000000000”
# Output: -1


def split(s):
    count = 0
    count_one = 0
    count_zero = 0
    for i in range(len(s)):
        if s[i] == 0:
            count_zero = count_zero + 1
        else:
            count_one = count_one + 1

        if count_zero == count_one:
            count = count + 1

    if count_zero != count_one:
        return -1
    return count


S = input()
ans = split(S)
print(ans)
