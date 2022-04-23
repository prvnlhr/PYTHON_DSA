# Given an array of words, print all anagrams together.
# For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”},
# then output may be “cat tac act dog god”.
from collections import defaultdict


def allAnagrams(wordList):
    map = defaultdict(list)

    for word in wordList:
        sortedWord = ''.join(sorted(word))
        map[sortedWord].append(word)

    print(map)
    for words in map.values():
        print(' '.join(words))


arr = ["cat", "dog", "tac", "god", "act"]

allAnagrams(arr)
