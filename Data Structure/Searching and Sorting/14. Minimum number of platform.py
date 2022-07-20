# Given the arrival and departure times of all trains
# that reach a railway station, the task is to find
# the minimum number of platforms required for the
# railway station so that no train waits.
# We are given two arrays that represent the arrival
# and departure times of trains that stop.

#
# Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}# dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
# Output: 3
# Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)
#
# Input: arr[] = {9:00, 9:40}
# dep[] = {9:10, 12:00}
# Output: 1
# Explanation: Only one platform is needed.


# All events are sorted by time.
# Total platforms at any time can be obtained by
# subtracting total departures from total arrivals
# by that time.
#
#  Time      Event Type     Total Platforms Needed
#                                at this Time
#  9:00       Arrival                  1
#  9:10       Departure                0
#  9:40       Arrival                  1
#  9:50       Arrival                  2
#  11:00      Arrival                  3
#  11:20      Departure                2
#  11:30      Departure                1
#  12:00      Departure                0
#  15:00      Arrival                  1
#  18:00      Arrival                  2
#  19:00      Departure                1
#  20:00      Departure                0
#
# Minimum Platforms needed on railway station
# = Maximum platforms needed at any time
# = 3
# Note: This approach assumes that trains are arriving
# and departing on the same date.

# TIME COMPLEXITY: O(N logN)
def minPlatforms(arr, dep):
    res = 0
    platForms = 0

    arr.sort()
    dep.sort()

    i = 0
    j = 0
    m = len(arr)
    n = len(dep)
    while i < m and j < n:
        if arr[i] < dep[j]:
            platForms += 1
            i += 1
        else:
            platForms -= 1
            j += 1
        res = max(res, platForms)
    return res


testCases = [
    [[9.00, 9.40],
     [9.10, 12.00]], [[9.00, 9.40, 9.50, 11.00, 15.00, 18.00],
                      [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]],
    [[2.00, 2.10, 3.00, 3.20, 3.50, 5.00], [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]]]

for arrival, departure in testCases:
    ans = minPlatforms(arrival, departure)
    print(ans)
