# O(n^2), O(N)


def threeSumZero(arr):
    arr.sort()
    res = []
    map = set()
    for i in range(len(arr)):
        ele = arr[i]

        start = i + 1
        end = len(arr) - 1

        while start < end:
            sum_of_three = ele + arr[start] + arr[end]

            if sum_of_three == 0:
                pair = (ele, arr[start], arr[end])
                if pair not in map:
                    map.add((ele, arr[start], arr[end]))
                    res.append([ele, arr[start], arr[end]])
                else:
                    start += 1

            elif sum_of_three < 0:
                start += 1
            elif sum_of_three > 0:
                end -= 1

    return res


# ____
def threeSum1(nums):
    nums.sort()
    map = set()
    res = []
    n = len(nums)

    for i in range(n - 1, -1, -1):
        ele = nums[i]
        start = i + 1
        end = n - 1

        while start < end:
            s = ele + nums[start] + nums[end]

            if s == 0:
                pair = (ele, nums[start], nums[end])
                if pair not in map:
                    map.add((ele, nums[start], nums[end]))
                    res.append([ele, nums[start], nums[end]])
                else:
                    start += 1

            elif s < 0:
                start += 1

            elif s > 0:
                end -= 1
    return res


# __________________________________________________________
# O(n^2) ,O(1)
def threeSumBetter1(nums):
    res = []  # Res to store Triplet
    n = len(nums)  # Length of the list
    nums.sort()  # We need to sort the list first!

    for i in range(n - 2):

        '''  
        Since the list is sorted, if nums[i] > 0, then all
        nums[j] with j > i are positive as well, and we cannot
        have three positive numbers sum up to 0. Return immediately.
        '''

        # EDGE CASE:
        if nums[i] > 0:
            break

        '''
        The nums[i] == nums[i-1] condition helps us avoid duplicates.
        E.g., given [-1, -1, 0, 0, 1], when i = 0, we see [-1, 0, 1]
        works. Now at i = 1, since nums[1] == -1 == nums[0], we avoid
        this iteration and thus avoid duplicates. 
        The i > 0 condition is to avoid negative index, i.e., 
        when i = 0, nums[i-1] = nums[-1] and you don't want to skip this 
        iteration when nums[0] == nums[-1]   
        '''

        # EDGE CASE 2 :: If first and next consecutive elements to it are same(duplicates)
        if i > 0 and nums[i] == nums[i - 1]:
            # skip till it does not become zero
            continue

        # Classic two pointer solution
        start = i + 1
        end = n - 1
        while start < end:
            s = nums[i] + nums[start] + nums[end]
            if s < 0:  # sum too small, move left ptr
                start += 1

            elif s > 0:  # sum too large, move right ptr
                end -= 1
            else:
                res.append([nums[i], nums[start], nums[end]])

                # We need to skip elements that are identical to our
                # current solution, otherwise we would have duplicated triples
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1

                start += 1
                end -= 1

    return res


# ___without comments
def threeSumBetter2(nums):
    res = []
    n = len(nums)
    nums.sort()

    for i in range(n - 2):

        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        start = i + 1
        end = n - 1
        while start < end:
            s = nums[i] + nums[start] + nums[end]

            if s == 0:
                res.append([nums[i], nums[start], nums[end]])
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1

                # after skipping, actual pointer movement,happens here.
                # the above loops just skips duplicates,and pointer is at element
                # which is included in s(sum), and as sum is done , we need to
                # still move pointer ,so below step is must
                # increment start++ , decrement end--
                start += 1
                end -= 1


            elif s < 0:
                start += 1

            elif s > 0:
                end -= 1

    return res


testCases = [[-1, 0, 1, 2, -1, -4], [0, -1, 2, -3, 1], [-2, 0, 0, 2, 2]]
# nums = [-1, 0, 1, 2, -1, -4]
# [[-1, -1, 2], [-1, 0, 1]]
# nums = [0, -1, 2, -3, 1]
# nums = [-1, 0, 1, 2, -1, -4]
# nums = [-2, 0, 0, 2, 2]
for nums in testCases:
    # ans = threeSumBetter2(nums)
    ans = threeSum1(nums)
    # ans = threeSumZero(nums)
    print(ans)
    print()
