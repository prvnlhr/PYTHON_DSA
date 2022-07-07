# Design an algorithm that collects daily price quotes for some
# stock and returns the span of that stock's price for the current day.
# The span of the stocks price today is defined as
# the maximum number of consecutive days (starting from today and going backward)
# for which the stock price was less than or equal to today's price.

# For example, if the price of a stock over the next 7 days were
# [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].


# INTUITION::
# stack = [0 ,  ,  ,  ,  ,  ,]
# output = [1 ,  ,  ,  ,  ,  ,]
# Well at start put first 0th index to stack and in output array
# put 1, because output for first price will be always 1
# now, iterate for rest price array from 1 to n
# for every price check if stack top index ele is smaller, if yes pop
# else put current index to stack, and if stack exists,
# then output at that index will be curr index - stack_top index
# else curr index + 1
#
# EXTENSION OF NGL(NEAREST GREATER TO LEFT OR NEXT GREATER TO LEFT)
def next(price):
    stack = []
    output = [1] * len(price)

    for i in range(len(price)):

        while stack and price[stack[-1]] <= price[i]:
            stack.pop()
        if stack:
            output[i] = i - stack[-1]
        else:
            output[i] = i + 1
        stack.append(i)
    return output


# arr = [int(i) for i in input().strip().split()]
testCases = [[100, 80, 60, 70, 60, 75, 85], [10, 4, 5, 90, 120, 80]]
for test in testCases:
    ans = next(test)
    print(ans)
#
