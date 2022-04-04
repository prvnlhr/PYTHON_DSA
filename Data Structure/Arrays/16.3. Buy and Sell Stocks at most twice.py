# In daily share trading, a buyer buys shares in the morning
# and sells them on the same day. If the trader is allowed to
# make at most 2 transactions in a day, whereas the second
# transaction can only start after the first one is complete (Buy->sell->Buy->sell).
# Given stock prices throughout the day, find out the maximum profit
# that a share trader could have made

# Example 1:
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
#
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later,
# as you are engaging multiple transactions at the same time.
# You must sell before buying again.
#
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# Input:   price[] = { 10, 22, 5, 75, 65, 80 }
# Output:  87
# Trader earns 87 as sum of 12, 75
# Buy at 10, sell at 22, 22 -10 = 12
# Buy at 5 and sell at 80 , 80 - 5 = 75
#
# Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
# Output:  100
# Trader earns 100 as sum of 28 and 72
# Buy at price 2, sell at 30, buy at 8 and sell at 80
#
# Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
# Output:  72
# Buy at price 8 and sell at 80.
# Input:   price[] = {90, 80, 70, 60, 50}
# Output:  0
# Not possible to earn.


# DP Solution__ Time complexity : O(n).
import sys


def maxProfits(prices):
    n = len(prices)
    # initialize dp with 0
    dp = [0 for _ in range(n)]

    # 0 <------------------- n-1
    max_price = prices[n - 1]
    for i in range(n - 2, 0, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        dp[i] = max(dp[i + 1], max_price - prices[i])
    #  0 ---------------------> n-1
    min_price = prices[0]
    for i in range(1, n):
        if prices[i] < min_price:
            min_price = prices[i]
        dp[i] = max(dp[i - 1], dp[i] + (prices[i] - min_price))

    ans = dp[n - 1]
    return ans


# Another O(N) solution O(1)
def maxProfit(price):
    first_buy = -sys.maxsize
    first_sell = 0
    second_buy = -sys.maxsize
    second_sell = 0

    for i in range(len(prices)):
        first_buy = max(first_buy, -price[i])
        first_sell = max(first_sell, first_buy + price[i])
        second_buy = max(second_buy, first_sell - price[i])
        second_sell = max(second_sell, second_buy + price[i])

    return second_sell


# Another O(N) solution O(1)
def maxProfit1(price):
    t1Cost = sys.maxsize
    t1Profit = 0
    t2Cost = sys.maxsize
    t2Profit = 0

    for i in range(len(prices)):
        currCost = price[i]  # current cost of stock

        # _______________THIS STEP IS SIMILAR TO BUY AND SELL-I  PROBLEM___________________________
        t1Cost = min(t1Cost, currCost)  # cost of buying first stock will be min(t1Cost,currCost)
        print("t1C", t1Cost)
        currFirstProfit = currCost - t1Cost
        print("P1", currFirstProfit)
        t1Profit = max(t1Profit, currFirstProfit)  # Profit from 1st transaction
        # _________________________________________________________________________________________
        # _______________AS WE ARE ALLOWED TO BUY STOCK AT MOST TWICE______________________________
        # THE ABOVE STEP IS REPEATED ONE MORE TIME , BUT THIS TIME t2Cost depends on t1Profit
        t2Cost = min(t2Cost, currCost - t1Profit)
        print("t2C", t2Cost)
        currSecondProfit = currCost - t2Cost
        print("P2", currSecondProfit)
        t2Profit = max(t2Profit, currSecondProfit)  # profit from second transaction
        print()
    print("_____________________________")
    return t2Profit


testCases = [[10, 22, 5, 75, 65, 80], [3, 3, 5, 0, 0, 3, 1, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
for test in testCases:
    prices = test
    ans = maxProfit1(prices)
    print(ans)
