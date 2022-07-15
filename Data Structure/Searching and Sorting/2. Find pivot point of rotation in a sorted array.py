def findPivot1(arr):
    lo = 0

    hi = len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        elif arr[mid - 1] > arr[mid]:
            return arr[mid]

        elif arr[0] < arr[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def findPivotOfRotation(arr):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[hi]:
            hi = mid
        else:
            lo = mid + 1

    return arr[hi]


# LEETCODE ______
# PRBLM 153. FIND MINIMUM IN SORTED ROTATED ARRAY,
# THIS PRBLM IS SAME AS FIND PIVOT.

def findMin(nums):
    # If the list has just one element then return that element.
    if len(nums) == 1:
        return nums[0]

    # left pointer
    left = 0
    # right pointer
    right = len(nums) - 1

    # if the last element is greater than the first element
    # then there is no rotation.
    # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
    # Hence the smallest element is first element. A[0]

    if nums[right] > nums[0]:
        return nums[0]

    # Binary search way____
    while right >= left:
        # Find the mid element
        mid = left + (right - left) // 2

        # if the mid element is greater than its next element
        # then mid+1 element is the smallest
        # This point would be the point of change. From higher to lower value.
        # 3  4  5  1  2
        #       |
        #      mid        arr[mid] > arr[mid+1]
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # if the mid element is lesser than its previous element
        # then mid element is the smallest
        #    5  6  1  2  3 
        #          |
        #         mid       arr[mid-1] > arr[mid]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # if the mid elements value is greater than the 0th element this means
        # the least value is still somewhere to the right as we are
        # still dealing with elements greater than nums[0]
        if nums[mid] > nums[0]:
            left = mid + 1

        # if nums[0] is greater than the mid value then this means
        # the smallest value is somewhere to the left
        else:
            right = mid - 1


arr = [4, 5, 6, 7, 8, 1, 2, 3]
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
arr = [16, 18, 22, 25, 1, 3, 5, 6, 7, 10, 14]
arr = [5, 6, 1, 2, 3, 4]
ans1 = findPivotOfRotation(arr)
ans2 = findPivot1(arr)
print(ans1, ans2)
