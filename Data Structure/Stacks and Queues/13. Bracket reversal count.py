# Input:  exp = "}{"
# Output: 2
# We need to change '}' to '{' and '{' to
# '}' so that the expression becomes balanced,
# the balanced expression is '{}'
#
# Input:  exp = "{{{"
# Output: Can't be made balanced using reversals
#
# Input:  exp = "{{{{"
# Output: 2
#
# Input:  exp = "{{{{}}"
# Output: 1
#
# Input:  exp = "}{{}}{{{"
# Output: 3


# LOGIC TO SOLVE::
# We will use the concept of balanced parenthesis problem
#  here.
# if for a given string of parenthesis, if we remove all the balanced parenthesis,
# what left is still need to be balanced.
# Consider ' } { { } { { { '
# After removing all balanced pairs we get , } { { {
# now , " } { { { " this is the left over string we still need to balanced
# if we find the count of this string, the we will get our ans.
# now how to get this count??
# } { { { , if we look carefully, from end of string
# if from end two char are same means we just need to reverse one to balanced them
# so our count will be 1
# now } { , for this , both need to be reverse ,so count will be 2
# so if two adjacent chars are same count is 1 ,else count is 2
#
# so problem boils down to
# first remove all balanced pairs
# second compute count for remaining unbalanced string

def countReversal(string):
    n = len(string)

    # edge case
    if n % 2 != 0:
        return -1

    stack = []

    for char in string:
        if char == '{':
            stack.append(char)

        elif char == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)

    count = 0
    while stack > 0:
        top1 = stack.pop()
        top2 = stack.pop()

        if top1 == top2:
            count = count + 1
        else:
            count += 2
    return count


string = input()
print(countReversal(string))
