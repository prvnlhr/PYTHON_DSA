# Ex_ 0 1 2 0 1 2
#     0 0 1 1 2 2

def sort012(nums):
    # _________SOL 1  T: O(N), S: O(1)
    # In first pass count number of 0's , 1's, 2's.
    # In second pass insert 0 1 and 2 according to counts
    countZero = 0
    countOne = 0
    countTwo = 0

    for i in range(len(nums)):
        # O(N)
        # Count zeros,ones,two
        if nums[i] == 0:
            countZero = countZero + 1
        if nums[i] == 1:
            countOne = countOne + 1
        if nums[i] == 2:
            countTwo = countTwo + 1
    # Replace element according to counts
    # O(N)
    for j in range(len(nums)):
        if (countZero > 0):
            nums[j] = 0.
            countZero = countZero - 1
        elif (countOne > 0):
            nums[j] = 1
            countOne = countOne - 1
        else:
            nums[j] = 2
            countTwo = countTwo - 1
    return nums


# ________________________________________________________________________________________________

# ___________SOL 2 , DUTCH NATIONAL FLAG APPROACH (GFG Solution) T: O(N), S: O(1)
# we have three pointer lo, mid, hi
# lo will point to zero
# mid will point to 1
# hi will point to 2
def sort012Better(arr):
    # INITIALLY::
    lo = 0
    hi = len(arr) - 1
    mid = 0

    # NOTE : mid will be used as iterator

    while mid <= hi:

        if nums[mid] == 0:  # if mid ele is == 0
            nums[lo], nums[mid] = nums[mid], nums[lo]  # swap it with lo,
            lo = lo + 1  # increase lo and mid
            mid = mid + 1



        elif nums[mid] == 1:  # if mid ele == 1
            mid = mid + 1  # increase mid

        else:  # if mid ele == 2 ,
            nums[mid], nums[hi] = nums[hi], nums[mid]  # swap it with hi,
            hi = hi - 1  # decrease hi

    return nums


nums = [int(i) for i in input().strip().split()]

ans = sort012(nums)
print(ans)
