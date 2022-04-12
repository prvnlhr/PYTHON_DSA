# Given an array of n distinct elements, find the minimum
# number of swaps required to sort the array.

# Input: {4, 3, 2, 1}
# Output: 2
# Explanation: Swap index 0 with 3 and 1 with 2 to
#               form the sorted array {1, 2, 3, 4}.
#
# Input: {1, 5, 4, 3, 2}
# Output: 2

# INTUITION::
# Well we can solve this problem if we know correct place
# of all elements then we can count and get minimum swaps
# SO here , we will sort the array and store it in temp array
# While iterating over the input array, check the current element,
# and if not in the correct place, replace that element with the
# index of the element which should have come in this place.


from collections import defaultdict


# OVERALL TIME COMPLEXITY : O(N*N)


def minSwaps(arr):
    sortedArray = arr.copy()
    sortedArray.sort()
    num_of_swaps = 0
    for i in range(len(arr)):  # O(N)
        if arr[i] != sortedArray[i]:
            num_of_swaps += 1
            index = getIndexOf(arr, sortedArray[i])  # O(N)
            swap(arr, i, index)
            print(arr)
    return num_of_swaps


# O(n)
def getIndexOf(arr, ele):
    for index in range(len(arr)):
        if arr[index] == ele:
            return index
    return -1


# O(1)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# ________________________________________________________________
# OPTIMISED
# Time Complexity: O(n Log n)
# Auxiliary Space: O(n)
# We can still improve the complexity by using a hashmap.
# The main operation here is the indexOf method inside the
# loop, which costs us n*n. We can improve this section to O(n),
# by using a hashmap to store the indexes. Still, we use the
# sort method, so the complexity cannot improve beyond O(n Log n)

def minSwapsOpt(arr):

    sortedArray = arr.copy()
    # O(nlogn)
    sortedArray.sort()
    map = defaultdict(list)

    for indx in range(len(arr)):
        map[arr[indx]] = indx

    # O(1)
    def getIndexOfFromMap(ele):
        return map[ele]

    # O(1)
    def swapEle(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def getMinSwaps():
        num_of_swaps = 0

        # O(n)
        for i in range(len(arr)):

            if arr[i] != sortedArray[i]:
                num_of_swaps += 1

                curr_original = arr[i]

                # get index of element and swap_______
                index = getIndexOfFromMap(sortedArray[i])
                swapEle(i, index)

                # Now as we have swapped the elements in input array______
                # we would need to also update their index in map

                # 1. as after swapping curr elem is gone to index,change it in map
                map[curr_original] = index
                # 2. and at curr index i  we got correct element ,which is tempArr[i],so change it also
                map[sortedArray[i]] = i

        return num_of_swaps

    ans = getMinSwaps()
    return ans


# Without comments_____________


def minSwapsOpt(arr):
    sortedArray = arr.copy()
    sortedArray.sort()

    map = defaultdict(list)

    for index in range(len(arr)):
        map[arr[index]] = index

    def getIndexOfFromMap(ele):
        return map[ele]


    def swapEle(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def getMinSwaps():

        num_of_swaps = 0
        for curr_index in range(len(arr)):

            if arr[curr_index] != sortedArray[curr_index]:
                num_of_swaps += 1

                originalEle = arr[curr_index]
                replaceWithEle = sortedArray[curr_index]

                new_index = getIndexOfFromMap(replaceWithEle)
                swapEle(curr_index, new_index)

                map[originalEle] = new_index
                map[replaceWithEle] = curr_index

        return num_of_swaps

    ans = getMinSwaps()
    print('ans',ans)
    return ans


# ________________________________________________________________
# arr = [1, 5, 4, 3, 2]
# arr = [2, 8, 5, 4]
arr = [8, 3, 14, 17, 15, 1, 12]
# arr = [4, 3, 2, 1]
ans1 = minSwapsOpt(arr)
print(ans1)

# [101, 315, 758, 730, 472, 619, 460, 479]
# [101, 315, 460, 730, 472, 619, 758, 479]
# [101, 315, 460, 472, 730, 619, 758, 479]
# [101, 315, 460, 472, 479, 619, 758, 730]
# [101, 315, 460, 472, 479, 619, 730, 758]


# [101, 315, 758, 730, 472, 619, 460, 479]
# [101, 315, 460, 730, 472, 619, 758, 479]
# [101, 315, 460, 472, 730, 619, 758, 479]
# [101, 315, 460, 472, 479, 619, 758, 730]
# [101, 315, 460, 758, 479, 619, 472, 730]
# [101, 730, 460, 758, 479, 619, 472, 315]
