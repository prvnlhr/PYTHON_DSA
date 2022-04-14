# There are n children standing in a line. Each child is assigned
# a rating value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute
# the candies to the children.
#
#
# Example 1:
#
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:
#
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.

# DRY RUN::
# ratings = [ 1, 3, 2, 2, 1 ]
# candies =   1  2  1  2  1   = 7

# Initially everyone will have one candy


#    candiesArray     1   1   1   1   1
#                     1   3   2   2   1

#
# traverse from left to right -->


#                       i
#                       |
#                   1   3   2   2   1        if arr[i-1] < arr[i] -> candy at candiesArray[i] needs to be
# candiesArray      1   2                    more then candiesArray[i-1] , so , candy at candiesArray[i] = candiesArray[i-1]+1
#
#                           i
#                           |
#                   1   3   2   2   1        if arr[i-1] > arr[i] -> do nothing
# candiesArray      1   2   1                so , candy at candiesArray[i] = remains same


#                               i
#                               |
#                   1   3   2   2   1        if arr[i-1] == arr[i] -> do nothing
# candiesArray      1   2   1   1            so , candy at candiesArray[i] = remains same


#                                   i
#                                   |
#                   1   3   2   2   1        if arr[i-1] > arr[i] -> do nothing
# candiesArray      1   2   1   1   1        candy at candiesArray[i] = remains same


# final array after left to right processing :

#                   1   3   2   2   1
# candiesArray      1   2   1   1   1


# Now, traverse from right to left  <-

#                                   i
#                                   |
#                   1   3   2   2   1        if arr[i-1] > arr[i] -> then candiesArray[i-1] needs to be more then candiesArray[i]
# candiesArray      1   2   1   2   1        so candy at candiesArray[i-1] = max(candiesArray[i-1],candiesArray[i]+1)
#                               |
#                            changed


#                               i
#                               |
#                   1   3   2   2   1        if arr[i-1] == arr[i] ->do nothing
# candiesArray      1   2   1   2   1        so candy at candiesArray[i-1] = remains same


#                           i
#                           |
#                   1   3   2   2   1        if arr[i-1] > arr[i] -> then candiesArray[i-1] needs to be more then candiesArray[i]
# candiesArray      1   2   1   2   1        so candy at candiesArray[i-1] = max(candiesArray[i-1],candiesArray[i]+1)
#                       |
#                       3 -> wrong ans, if we simply do candiesArray[i-1] = candiesArr[i] + 1

#                    now, arr[i-1] > (greater) arr[i]  ->  so we have to increase , candiesArray[i-1] = candiesArr[i]+1
#                             |          |                 therefore ,candiesArray[i-1] = 2 + 1 = 3, but this gives wrong ans,
#                             3          2                 because, we see that candiesArr[i-1] is 2 which is already greater
#                                                          then candiesArr[i] , so we need not to increase
#                                         Hence, correct step will be to , do ''' max(candiesArr[i-1],candiesArr[i]+1) '''
#


# T: O(N)
# S: O(N)
def candyDist(ratings):
    n = len(ratings)

    ans = [1 for i in range(n)]

    for i in range(1, n):
        if ratings[i - 1] < ratings[i]:
            ans[i] = ans[i - 1] + 1

    for i in range(n - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            ans[i - 1] = max(ans[i - 1], ans[i] + 1)

    # OR__
    # for i in range(n - 2, 0, -1):
    #     if ratings[i] > ratings[i + 1]:
    #         ans[i] = max(ans[i], ans[i + 1] + 1)

    return sum(ans)


ratings = [1, 3, 2, 2, 1]
# ratings = [0, 1, 20, 9, 8, 7]
# ratings = [1, 2, 2]
ans = candyDist(ratings)
print(ans)
