# REFER STRIVER'S YT VIDEO
# APPROACH::

# Given an arr of n books with pages in it and no. of students to
# allocate books, m = 2,  [12 , 34,  67,  90]
# We have to find the '''minimum of maximum''' of minimum pages allocated to m students
# Consider  m = 2, [12 , 34,  67,  90]
#
#  s1(Student 1)          :        s2(student 2)
#  12                              34 + 67 + 90 == 191 ,   min = 12 , max = 191
#  12 + 34 == 46                   67 + 90 ==  157 ,       min = 46 , max = 157
#  12 + 34 + 67 == 113             90                      min = 90 , max = 113

# So max = 113 , which is minimum of all max, and it is our ans

# SO WHAT IS SOL ???
# We can solve is recursively with all the possible allocation cases
# Time complexity would be 2^n

# BETTER SOL ::
# BINARY SEARCH SOLUTION  , O(nLogN)

# What is the minimum number of pages can be allocated if only one student is there ??
# The ans would be minimum of array or 0
# What would be max , ans is sum of all pages of all books
# So now we have min and max , or lo or hi
# Now find the mid of min ,max or (lo,hi)
# mid = (lo,hi)//2
# now our mid could be ans , if we could allocate all books to all students, considering mid as our ans
# So we will find if mid is our feasible ans or not.
# if we found that mid can be our ans so we will try to further minimise by reducing our lo, hi range from lo to mid-1
# else we will increase our range from mid+1 to  hi
#
# Now for a a mid value how to find if it is feasible ans or not,
# our isPossible function will give us ans.
# We will keep a variable allocatedStudent  = 1
# for every book we will allocate it to student no 1 , and increase pagesAllocated
# if pagesAllocated is less that our mid value we can still allocate pages to student 1
# At last if all students are allocated all book we have our ans True or False
import sys


# T : O(N) +O(logN) = O(NlogN)

# NOTE: In interview don't waste time on suggesting or working on brute force sol,
#       because it is complex to work out and will waste lot of time.
#       So directly jump on optimize binary search solution.


# O(N)
def isPossible(arr, pages_barrier, students):
    allocatesStudents = 1
    pagesAllocates = 0

    for i in range(len(arr)):

        if arr[i] > pages_barrier:
            return False

        if pagesAllocates + arr[i] > pages_barrier:
            allocatesStudents += 1
            pagesAllocates = arr[i]
            if allocatesStudents > students:
                return False
        else:
            pagesAllocates += arr[i]

    return True


# OR, similar to above just if else conditions are reversed
def possible(arr, pages_barrier, students):
    pagesAllocated = 0
    allocatedStuds = 1
    for i in range(len(arr)):

        if arr[i] > pages_barrier:
            return False

        if pagesAllocated + arr[i] <= pages_barrier:
            pagesAllocated += arr[i]
        else:
            allocatedStuds += 1
            pagesAllocated = arr[i]
            if allocatedStuds > students:
                return False
    return True


# O(logN)
def booksAllocate(arr, students):
    n = len(arr)
    if n < students:
        return -1
    lo = arr[0]
    hi = sum(arr)
    res = -1
    while lo <= hi:

        mid = (lo + hi) // 2
        if possible(arr, mid, students):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return res


arr = [12, 34, 67, 90]
# arr = [31, 14, 19, 75]

ans = booksAllocate(arr, 2)
print(ans)
