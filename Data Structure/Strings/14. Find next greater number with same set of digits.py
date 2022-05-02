# Given a number n, find the smallest number that has same
# set of digits as n and is greater than n. If n is the
# greatest possible number with its set of digits, then print “not possible”.
#
# Examples:
# For simplicity of implementation, we have considered
# input number as a string.
#
# Input:  n = "218765"
# Output: "251678"
#
# Input:  n = "1234"
# Output: "1243"
#
# Input: n = "4321"
# Output: "Not Possible"
#
# Input: n = "534976"
# Output: "536479"

# This problem is same as next greater number represent by array

def nextGreaterNumber(s):
    s = [str(char) for char in s]
    j = len(s) - 2
    # 1. Find the index of first element which is smaller then right of it
    while j >= 0:
        if s[j] < s[j + 1]:
            break
        j = j - 1

    # EDGE CASE:
    if j < 0:
        s = s[::-1]

    else:
        # 2. Find first greater element from above found element
        # we are starting from end left-side,because we
        # know all elements will be in decreasing order ,
        # this is optimized compare to travelling to right-side
        for i in range(len(s) - 1, j, -1):
            if s[i] >= s[j]:
                break
        s[i], s[j] = s[j], s[i]

        # 3. Reverse elements from j right side
        print(s, j)
        s[j + 1:] = reversed(s[j + 1:])

    return s


s = input()
ans = nextGreaterNumber(s)
print(ans)
