# There are n gas stations along a circular route,
# where the amount of gas at the ith station is gas[i].
#
# You have a car with an unlimited gas tank and it costs
# cost[i] of gas to travel from the ith station to its
# next (i + 1)th station. You begin the journey with an
# empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting
# gas station's index if you can travel around the circuit
# once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique
#
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:
#
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.

# https://leetcode.com/problems/gas-station/discuss/860347/Python-simple-and-very-short-explained-solution-O(n)-O(1)-faster-than-98
# If sum of gas is less than sum of cost,
# then there is no way to get through all
# stations. So while we loop through the
# stations we sum up, so that at the end
# we can check the sum.
# Otherwise, there must be one unique
# solution, so the first one I find is
# the right one. If the tank becomes
# negative, we restart because that can't happen.


def circularTour(gas, cost):
    # edge case
    print(sum(gas))
    print(sum(cost))
    # if we have less gas then cost, no solution exists
    if (sum(gas) - sum(cost)) < 0:
        return -1


    # if above condition, is not satisfied, means there a valid solution,
    # i.e there is a starting point exists, from where we can do a circular tour.
    # We just need to find that starting point.
    # after finding start point we don't need to check if circular tour can be
    # done because, if first condition is false, then we will always have a circular path.
    n = len(gas)
    gas_tank = 0
    start_index = 0
    for i in range(n):
        gas_tank += gas[i] - cost[i]
        if gas_tank < 0:
            start_index  = i+1
            gas_tank = 0

    return start_index





gas = [int(i) for i in input().strip().split()]
cost = [int(j) for j in input().strip().split()]
ans = circularTour(gas, cost)
print(ans)
