import bisect
import sys
from collections import Counter, defaultdict


# There is a song concert going to happen in the city. There are ‘N’
# tickets available for the concert each with a certain price.
# The prices of ‘N’ tickets are given in an ‘N’ sized ‘price’ array.
# There are ‘M’ customers which come one by one in order to buy a ticket.
# Each customer offers a maximum price he or she can pay to buy a ticket.
# The maximum price offered by ‘M’ customers are given in an ‘M’ sized ‘pay’
# array. The customer will get the ticket at the nearest possible price
# which will not exceed their offered maximum price. Your task is to
# return the price at which each customer will buy a ticket. If a
# particular is not able to buy the ticket, then consider -1 as the
# ticket cost in that case.


# 5 3 7 8 5
# 4 8 3

# here are 5 tickets with prices as {5, 3, 7, 8, 5}, and the number of
# customers to buy tickets are 3. The first person comes and offers a
# maximum price of 4 units so he gets the ticket by paying 3 units as price.
# The tickets left are {5, 7, 8, 5}. The second person comes and offers a
# maximum price of 8 units so he gets the ticket by paying 8 units as price.
# The tickets left are {5, 7, 5}. The third person comes and offers a maximum
# price of 3 units so he will not get the ticket as there is no ticket left
# with a price less than or equal to 3. So the output is {3, 8 , -1}.

# https://www.codingninjas.com/codestudio/problems/concert-tickets_1496516?leftPanelTab=2

# Time Complexity
# O(M*N), where ‘N’ is the total number of tickets and ‘M’ is the total number of customers.
# Since for every customer we are traversing through the price array
# which takes a total of O(N) time per customer. So overall time
# complexity will be O(M*N).


def concertTickets(price, pay):
    res = []
    price.sort()

    def binarySearch(ele):

        ans = -1
        i = len(price) - 1

        while i >= 0:
            if price[i] < ele:
                ans = price[i]
                price[i] = sys.maxsize
                return ans


            elif price[i] == ele:
                ans = price[i]
                price[i] = sys.maxsize
                return ans

            i -= 1
        return ans

    for index, ele in enumerate(pay):
        found = binarySearch(ele)
        res.append(found)

    return res


# TIME COMPLEXITY :
# Worst case T :O((M+N)*Log(N)), where ‘N’ is the total number of
# tickets and ‘M’ is the total number of customers.
# Since we are inserting all the values of the price array into our multiset
# maxPrice which takes O(N*Log(N)) time. Traversing through each customer
# will take O(M) time, finding its upper bound in the price array and
# erasing the element from the price array will take in a total of O(M*Log(N)) time.
# So overall time complexity will be O((M+N)*Log(N)).


# Upper Bound Technique
# 1. Since we need to find the ticket with a price less than or equal to
# the maximum price offered by each customer. So we will use the
# upper bound to fulfill this purpose.
# 2. Now to use the upper bound the price array should be sorted and it can
# have duplicate values so we will insert all the values of the price
# array in a multiset which will fulfill our requirements.
# 3. Since the upper bound will give us the iterator pointing to the
# first element greater than the value passed as a parameter.
# So for each value of maximum price offered by the customer, we will
# find its upper bound in the multiset and get an iterator to it.
# 4. If the iterator is pointing at the beginning then that means there
# are no tickets that are less than or equal to the maximum price offered.
# Otherwise, decrement the iterator to make the iterator point to a value
# less than or equal to the maximum price offered by the customer and print
# the value pointed by that iterator and erase that element from the multiset
# as this ticket has been sold.

def concertTicketsBeetr(price, pay):
    maxPrice = sorted(price)
    res = [0] * len(pay)

    for i, ele in enumerate(pay):
        pos_of_ele = bisect.bisect(maxPrice, ele)

        if pos_of_ele == 0:
            res[i] = -1
        else:
            # since bisect gives pos of ele in array not index, so we need to do (pos-1) to get index
            pos_of_ele -= 1
            res[i] = maxPrice[pos_of_ele]
            maxPrice.remove(res[i])  # remove used value from arr, to avoid taking it next time
    return res


prices = [5, 3, 7, 8, 5]
pay = [4, 8, 3]
# prices = [10, 10, 10, 10]
# pay = [10, 1, 1, 1]
# prices = [1, 2, 2]
# prices = [1, 2, 3]
# pay = [2, 2]
otp = concertTicketsBeetr(prices, pay)
print(otp)
