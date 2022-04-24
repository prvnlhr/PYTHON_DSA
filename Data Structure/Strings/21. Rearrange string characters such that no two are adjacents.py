from heapq import *


# Ex__ aab --> O/P --> aba
# Ex__ aaab --> O/P --> abaa, so not possible to rearrange
#
# IDEA TO SOLVE:
# We will maintain a max heap to get letter with the highest freq.
# 1. Initially we will put all the elements to map with their freq
# 2. Then we will put all the elements from the map to maxHeap
# 3. Then we will run a while loop till maxHeap  does not become empty
# 4. Pop a element from maxHeap, which will give letter with highest freq

# 5. put it into result array and decrease the freq count
#    5.1. if prevFreq is not zero means will still have a letter which is not exhausted so we will
#         put back to  maxHeap
# 6. now , update prevFreq = frequency and prevLetter = letter

# 7. At the end if len of result array string is equal to len of S will were able to make or rearrange,
#    string so return it else return empty string
#
def rearrangeString(S):
    frequencyDict = dict()

    for letter in S:
        if letter in frequencyDict:
            frequencyDict[letter] += 1
        else:
            frequencyDict[letter] = 1

    maxHeap = []

    for letter in frequencyDict:
        freq = frequencyDict[letter]
        # NOTE: we are taking negative value of frequency because by default
        # heaps are min heap, so to make it maxHeap on basis of freq we use negative value
        heappush(maxHeap, (-freq, letter))

    prevfreq = 0
    prevLetter = None
    result = []
    while maxHeap:
        frequency, letter = heappop(maxHeap)
        result.append(letter)

        # decreasing the frequency, by adding one as freq we
        # have in max_heap is -ve ,so -ve + +ve = -ve
        frequency = frequency + 1

        # we are holding the curr pop element from heap in prevLetter
        # because if we put again into heap we might get it again.
        if prevfreq != 0:
            heappush(maxHeap, (prevfreq, prevLetter))
        prevfreq = frequency
        prevLetter = letter

    result = ''.join(result)

    if len(result) == len(S):
        return result
    else:
        return ''


S = input()
print(rearrangeString(S))
