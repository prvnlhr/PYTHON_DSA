import sys


# You are given an integer array prices where prices[i] is the
# price of a given stock on the ith day, and an integer k.
#
# Find the maximum profit you can achieve. You may complete
# at most k transactions.
#
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).


# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
#
# Example 2:
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
# Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


# Time complexity : O(kn) , Space complexity : O(nk).


# REFER KEERTI PURSWANI YT VIDEO

def maxProfit(prices, k):
    n = len(prices)

    profit = [[0 for _ in range(n + 1)] for j in range(k + 1)]

    for i in range(1, k + 1):
        prev_diff = -sys.maxsize
        for j in range(1, n):
            prev_diff = max(prev_diff, profit[i - 1][j - 1] - prices[j - 1])
            profit[i][j] = max(profit[i][j - 1], prices[j] + prev_diff)

    return profit[k][n - 1]


prices = [int(i) for i in input().strip().split()]
k = int(input())
ans = maxProfit(prices, k)
print(ans)
