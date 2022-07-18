#   Job_id  deadline    profit
#      1        4        20
#      2        5        60
#      3        6        70
#      4        6        65
#      5        4        25
#      6        2        80
#      7        2        10
#      8        2        22

# How to solve ?
# first , we will consider job_id {6} which has max profit i.e -> 80
# job_id {6} with profit 80 have deadline of 2 , so it can be completed on day 1 or 2
# So we will complete it on day 2 i.e last day so that we get time for other jobs.

# Next we will select job_id {3} with profit 70. It can be completed on 1,2,3,4,5,6.
# We will do it on last day 6th.

# Next we will select job_id {4} with profit 65. It can be completed on 1,2,3,4,5,6.
# Now we can do it on 6th day because we have selected job_id {3} to do on 6th day,
# so we will do it on 5th day.

# Next we will select job_id {2} with profit 60. It can be completed on 1,2,3,4,5.
# We will do it on 4th day because we have assigned 5th day to job_id {4}.

# Next we will select job_id {5} with profit 25. It can be completed on 1,2,3,4.
# We will do it on 3rd day because we have assigned 4th day to job_id {3}.

# Next we will select job_id {8} with profit 22. It can be completed on 1,2.
# We will do it on 1st day because we have assigned 2nd day to job_id {6}.

#                                                      select job    can be completed
#   '''Sort according to profits'''                    with profit   on these days(deadline)
#   Job_id  deadline    profit                         80 -->        1, (2)
#      6        2        80                          + 70 -->        1, 2, 3, 4, 5, (6)
#      3        6        70                          + 65 -->        1, 2, 3, 4, (5), 6
#      4        6        65                          + 60 -->        1, 2, 3, (4), 5
#      2        5        60                          + 25 -->        1, 2, (3), 4
#      5        4        25                          + 22 -->        (1), 2
#      8        2        22                         -------------
#      1        4        20                         maxProfit = 322
#      7        2        10


# See striver's YT video
# T : O(NlogN) + O(M*N)
# S : O(M)
def jobSequencing(arr):
    # Sort based on profits in decreasing order.
    # O(NlogN)
    arr.sort(key=lambda x: x[2], reverse=True)
    # Find max deadline job,
    maxDeadline = 1
    for job in arr:
        maxDeadline = max(job[1], maxDeadline)

    jobSequence = [-1] * (maxDeadline + 1)

    maxProfit = 0
    countJobs = 0
    # TOTAL: O(N * M)
    for i in range(len(arr)):  # M
        jobNo, deadline, profit = arr[i][0], arr[i][1], arr[i][2]
        for j in range(deadline, 0, -1):  # N
            if jobSequence[j] == -1:
                jobSequence[j] = jobNo
                maxProfit += profit
                countJobs += 1
                break

    # Just putting only the job which are not -1 after completion,
    result = [ans for ans in jobSequence if ans != -1]
    return result, maxProfit


testCases = [[[1, 4, 20],
              [2, 5, 60],
              [3, 6, 70],
              [4, 6, 65],
              [5, 4, 25],
              [6, 2, 80],
              [7, 2, 10],
              [8, 2, 22]
              ], [
                 [1, 9, 15],
                 [2, 2, 2],
                 [3, 5, 18],
                 [4, 7, 1],
                 [5, 4, 25],
                 [6, 2, 20],
                 [7, 5, 8],
                 [8, 7, 10],
                 [9, 4, 12],
                 [10, 3, 5]
             ], [['a', 2, 100],
                 ['b', 1, 19],
                 ['c', 2, 27],
                 ['d', 1, 25],
                 ['e', 3, 15]]]

for arr in testCases:
    res = jobSequencing(arr)
    print('jobs Sequence :', res[0])
    print('maxProfit :', res[1])
    print()
