# Leetcode :
# '''THIS PROBLEM IS VARIATION OF ACTIVITY SELECTION PROBLEM'''


# There are some spherical balloons taped onto a flat wall that represents the XY-plane.
# The balloons are represented as a 2D integer array points where points[i] = [xstart, xend]
# denotes a balloon whose horizontal diameter stretches between xstart and xend. You do
# not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points
# along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up
# infinitely, bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


# Simplifying problem statement,
# We are given a points array , which has a [start, end] at every index,
# points : [[10,16],[2,8],[1,6],[7,12]]
# Now what this start and end represents , how much a balloon is stretched on x axis,

#       start     1   2   7   10
#       end       6   8   12  16
#     ._____. -> represents stretched of a balloon

#                                                                                    .10_______________________________________16.

#                                                                  .7_______________________________12.

#                                    .2___________________________________8.

#                              .1_____________________________6.
#                       ____0___1_____2_____3_____4_____5_____6_____7_____8_____9_____10_____11_____12_____13_____14_____15_____16___
#
# Now if we carefully look, if we shoot a arrow to first balloon (1,6), then balloon (2,8) will also burst, because they overlap
# so we need 1 arrow for (1,6) and (2,8).
# But, balloon (7,12) doesnt burst with same arrow,although it is also overlapping with  (2,8) why ??
# If we carefully observe, we see that the max range of first arrow will be  x = 6  which was shot to burst first arrow.
# As for the balloon (7,8) start is 7 which is more then the end-> 6 of first balloon (1,6).
# So we need one more arrow for balloon (7,8).
# Now in the case for balloon (10,16) is will burst with arrow shot for balloon (7,12) because its start ->10 is smaller
# then end of (7,12).


# Example 1:
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2

# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

# Example 2:
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

# Example 3:
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].


# SELF SOLVED 100% passed, submitted on Leetcode
def minNumofArrows(points):
    points = sorted(points, key=lambda x: x[1])

    arrows = 0  # stores output

    # as a points array is sorted on the basis of their end distance,
    # the maxRange_of_arrow specifies, the max range of array shot.
    maxRange_of_arrow = -float('inf')

    for interval in points:
        start = interval[0]
        end = interval[1]

        # IMP condition , if start of any balloon is not in maxRange_of_arrow then,
        #                 it will not bust and will will need one more arrow and also
        #                 maxRange_of_arrow will also be updated to curr balloons end.

        if start > maxRange_of_arrow:
            maxRange_of_arrow = end
            arrows += 1
    return arrows


testCases = [[[10, 16], [2, 8], [1, 6], [7, 12]], [[1, 2], [3, 4], [5, 6], [7, 8]], [[1, 2], [2, 3], [3, 4], [4, 5]]]

for points in testCases:
    ans = minNumofArrows(points)
    print(ans)
