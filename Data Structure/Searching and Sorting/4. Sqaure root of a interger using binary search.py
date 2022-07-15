import math


# T: O(logN)_
def findSqrt(n):
    if n == 0 or n == 1:
        return n
    lo = 1
    hi = n
    ans = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * mid == n:
            return mid

        if mid * mid < n:
            lo = mid + 1
            ans = mid
        else:
            hi = mid - 1
    return ans


# METHOD 2__
# T: O(1),O(1)

def findSqrt1(n):
    result = n ** 0.5
    return int(result)


n = 11
ans = findSqrt(n)
ans2 = findSqrt1(n)
print(ans, ',', ans2)
