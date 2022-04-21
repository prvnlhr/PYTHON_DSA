# EX_ ABC
# ABC
# ACB
# BAC
# BCA
# CBA
# CAB
#

# 1


result = []


def permutationHelper(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permutationHelper(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


# This does not prints duplicates permutation
def permute(s, answer):
    if (len(s) == 0):
        result.append(answer)
        return

    for i in range(len(s)):
        ch = s[i]
        # Create new Str for next function call
        left_subStr = s[:i]
        right_subStr = s[i + 1:]
        newStr = left_subStr + right_subStr

        permute(newStr, answer + ch)


def permutation(s):
    permutationHelper(list(s), 0, len(s))


s = input()
# permutation(s)
permute(s, '')
print(str(result))
