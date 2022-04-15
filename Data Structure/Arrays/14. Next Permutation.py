# Input: N = 6
# arr = {1, 2, 3, 6, 5, 4}
# Output: {1, 2, 4, 3, 5, 6}
# Explanation: The next permutation of the
# given array is {1, 2, 4, 3, 5, 6}

def nextPermutation(arr):
    # step1: finding first decreasing element moving towards left side
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i = i - 1
    # step2: finding next largest element moving from left to right side
    if i >= 0:
        j = len(arr) - 1
        while j >= 0 and arr[j] <= arr[i]:
            j = j - 1

        # step3: swap
        arr[i], arr[j] = arr[j], arr[i]

    # step4: reversing i+1 right side elements
    k = i + 1
    l = len(arr) - 1
    while k < l:
        arr[k], arr[l] = arr[l], arr[k]
        k = k + 1
        l = l - 1
    return arr


def nextPermutationBetter(arr):
    n = len(arr)

    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i < 0:
        arr = arr[::-1]
    else:

        j = n - 1

        for j in range(n - 1, i, -1):
            if arr[i] <= arr[j]:
                break

        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1:] = reversed(arr[i + 1:])

    return arr


def nextPermutation1(nums):
    i = len(nums) - 1
    while nums[i - 1] >= nums[i]:
        i -= 1

    i = i - 1

    if i < 0:
        nums = nums[::-1]


    else:
        swap1 = i
        j = len(nums) - 1
        while nums[j] <= nums[swap1]:
            j -= 1

        nums[swap1], nums[j] = nums[j], nums[swap1]

        i = i + 1
        l = len(nums) - 1
        while i <= l:
            nums[i], nums[l] = nums[l], nums[i]
            i += 1
            l -= 1
    return nums


# MOST CORRECT WORKS:
# ALL EDGE CASES HANDLED
def nextPermute(nums):
    # To reverse
    def reverse(startI, endI):
        while startI <= endI:
            nums[startI], nums[endI] = nums[endI], nums[startI]
            startI += 1
            endI -= 1

    # to swap
    def swap(indx1, indx2):
        nums[indx1], nums[indx2] = nums[indx2], nums[indx1]

    length = len(nums)
    i = length - 1

    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    i = i - 1
    swapIndex1 = i
    # if swapIndex < 0 means we just need tow reverse and return
    if swapIndex1 < 0:
        return nums[::-1]

    # else perform further operations
    else:
        j = length - 1
        while nums[i] >= nums[j]:
            j -= 1
        swapIndex2 = j

        swap(swapIndex1, swapIndex2)
        start = i + 1
        end = length - 1

        reverse(start, end)
        return nums


# arr = [int(i) for i in input().strip().split()]
arr = [1, 2, 3, 6, 5, 4]
# arr = [3, 2, 1]
# arr = [1, 1]
arr = [1, 2, 3]
print(arr)
ans = nextPermute(arr)
# ans = nextPermutationBetter(arr)
print(ans)
