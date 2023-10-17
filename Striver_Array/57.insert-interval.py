#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        if len(intervals) == 0:
            return [newInterval]

        start = -1
        for index, interval in enumerate(intervals):

            if start >= 0:
                if interval[1] <= intervals[start][1]:
                    intervals[index] = None
                elif interval[0] <= intervals[start][1]:
                    intervals[start][1] = max(interval[1], newInterval[1])
                    intervals[index] = None
                
                continue

            if (interval[0] <= newInterval[0] <= interval[1]) or (interval[0] <= newInterval[1] <= interval[1]):
                intervals[index] = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                start = index
            elif (newInterval[0] <= interval[0] <= newInterval[1]) or (newInterval[0] <= interval[1] <= newInterval[1]):
                intervals[index] = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                start = index

        if start < 0:
            return sorted(intervals + [newInterval])
            
        return sorted([i for i in intervals if i])








        # isBegin = True
        # res = []
        # for index, interval in enumerate(intervals):

        #     if isBegin and (interval[0] <= newInterval[0] <= interval[1]):
        #         x = min(interval[0], newInterval[0])
        #         isBegin = False
        #         start = index

        #     elif (not isBegin) and (interval[0] <= newInterval[1] <= interval[1]):
        #         y = max(interval[1], newInterval[1])
        #         res = intervals[:start]  + [[x, y]] + intervals[index+1:]
        #         break
                
        # return res

        
# @lc code=end

print(Solution().insert([[1,5]], newInterval = [0,6]))
# print(Solution().insert([[4,5],[6,9]], newInterval = [1,3]))

# print(Solution().insert([[1,3],[6,9]], newInterval = [2,5]))
# print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
