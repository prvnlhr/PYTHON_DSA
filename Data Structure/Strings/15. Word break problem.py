# Given an input string and a dictionary of words,
# find out if the input string can be segmented into
# a space-separated sequence of dictionary words.
# See following examples for more details.
# This is a famous Google interview question, also
# being asked by many other companies now a days.
#
# Consider the following dictionary
# { i, like, sam, sung, samsung, mobile, ice,
#   cream, icecream, man, go, mango}
#
# Input:  ilike
# Output: Yes
# The string can be segmented as "i like".
#
# Input:  ilikesamsung
# Output: Yes
# The string can be segmented as "i like samsung"
# or "i like sam sung".


def wordBreak(wordList, word):
    if word == '':
        return True
    if not word:
        return True
    length = len(word)
    for i in range(1, length + 1):
        prefix = word[:i]
        if prefix in wordList and wordBreak(wordList, word[i:]):
            return True
    return False


