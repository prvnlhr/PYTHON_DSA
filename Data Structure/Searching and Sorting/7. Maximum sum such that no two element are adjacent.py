# RECURSIVE CODE


def maxSum1(arr):
    def find(n):
        if n <= 0:
            return 0
        sum1 = arr[n - 1] + find(n - 2)
        sum2 = find(n - 1)
        return max(sum1, sum2)

    return find(len(arr))


def maxSum(arr):
    def findSum(arr, n):
        if n <= 0:
            return 0

        a = arr[n] + findSum(arr, n - 2)
        b = findSum(arr, n - 1)
        return max(a, b)

    return findSum(arr, len(arr) - 1)


# AS THE ABOVE CODE HAS OVERLAPPING SUB PROBLEMS
# WE CAN USE DP


def maxSumDP(arr):
    def findSum(arr):
        n = len(arr)
        dp = [0 for i in range(n + 1)]
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])

        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(1, n):
            a = arr[i] + dp[i - 2]
            b = dp[i - 1]
            dp[i] = max(a, b)
        return dp[n - 1]

    return findSum(arr)


# arr = [5, 5, 10, 40, 50, 35]
# arr = [1, 20, 3]
arr = [5, 5, 10, 100, 10, 5]
print(maxSumDP(arr))
print(maxSum1(arr))
