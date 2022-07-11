import queue
from collections import defaultdict


# Given a stream of characters and we have to find first
# non repeating character each time a character is inserted to the stream.

# ex_ aabccdba

# Incoming character  |  first non-rep
#     string          |    till now
# --------------------------------------------------
# a                   |   a
# aa                  |  -1
# aab                 |   b
# aabc                |   b
# aabcc               |   b
# aabccd              |   b
# aabccdb             |   d
# aabccdba            |   d

# INTUITION::
# take char one by one
# for every char, check if it is in map or not
# if in map increase frequency +1
# if not in map insert in map with frequency 1 ,and also in queue

# now once we are done with inserting in map,
# now if queueTop(queue[0]) has freq == 1 means, it is first non repeating,
# other wise we should remove it from queue as its frequency is more then 1,
# so we will run a while loop to check top of queue,and remove until its freq in map
# is  freq > 1.


def firstNonRepeating(s):
    map = defaultdict()
    q = queue.Queue()

    res = [-1] * (len(s))
    res_index = 0
    ans = ''

    for char in s:
        if char in map:  # if char in map increase freq + 1
            map[char] += 1

        elif char not in map:  # if not in map ,insert in map
            map[char] = 1
            q.put(char)  # also insert in queue

        # if queueTop element has freq > 1, i.e repeating, remove it from queue
        while not q.empty() and map[q.queue[0]] > 1:
            q.get()


        # after removing unwanted from queue
        if q.empty() == False:  # if still queue has element, we have non-repeating at queue[0]
            res[res_index] = q.queue[0]
            res_index += 1
        else:  # else if queue empty means no non  repeating, so -1 is ans
            res[res_index] = -1
            res_index += 1
    return res


testCases = ['aabc', 'aac', 'aabccdba']
for test in testCases:
    ans = firstNonRepeating(test)
    print(ans)
