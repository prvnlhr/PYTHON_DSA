# You are given n activities with their start and finish times. Select the
# maximum number of activities that can be performed by a single person,
# assuming that a person can only work on a single activity at a time.

# Example 1 : Consider the following 3 activities sorted by
# by finish time.
#      start[]  =  {10, 12, 20};
#      finish[] =  {20, 25, 30};

# A person can perform at most two activities. The
# maximum set of activities that can be executed
# is {0, 2} [ These are indexes in start[] and
# finish[] ]


# Example 2 : Consider the following 6 activities
# sorted by by finish time.
#      start[]  =  {1, 3, 0, 5, 8, 5};
#      finish[] =  {2, 4, 6, 7, 9, 9};
# A person can perform at most four activities. The
# maximum set of activities that can be executed
# is {0, 1, 3, 4} [ These are indexes in start[] and
# finish[] ]

# T: O(NlogN) if activities are not sorted
#    O(N) if sorted.


def activitySelection(activities):
    activities = sorted(activities, key=lambda x: x[1])
    numActivity = 0
    maxEndingTime = -float('inf')

    for activity in activities:
        start = activity[0]
        end = activity[1]
        if (start >= maxEndingTime):
            maxEndingTime = end
            numActivity += 1
    return numActivity


# for simplicity we are combining the input start and end time
# into a single array.


testCases = [[[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]], [[10, 20], [12, 25], [20, 30]],
             [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]]

for activities in testCases:
    ans = activitySelection(activities)
    print(ans)
