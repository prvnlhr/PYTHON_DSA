# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the
# ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that
# represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
#
#
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:
            # the new interval is after the range of other interval, so we can leave the current interval baecause the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval 
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)
        return result


obj = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
ans = obj.insert(intervals, newInterval)
print(ans)
