# Given a string, Find the 1st repeated word in a string
# Examples:
#
# Input : "Ravi had been saying that he had been there"
# Output : had
#
# Input : "Ravi had been saying that"
# Output : No Repetition
#
# Input : "he had had he"
# Output : he
from collections import defaultdict


def firstRepeatingWord(s):
    map = defaultdict(lambda: 0)

    stringArray = s.split(' ')

    for word in stringArray:
        map[word] = map[word] + 1

        if map[word] > 1:
            return word
    return 'no word is being repeated'


str = input()
ans = firstRepeatingWord(str)
print(ans)
