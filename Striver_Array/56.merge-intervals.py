#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        # print(intervals)
        # return

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            i1 = res[-1]
            i2 = intervals[i]

            if i1[0] <= i2[0] <= i1[1]:
                res[-1] = [i1[0], max(i1[1], i2[1])]
            elif i2[0] <= i1[0] <= i2[1]:
                res[-1] = [i2[0], max(i1[1], i2[1])]
            else:
                res.append(i2)



        # print(res)
        return res



        
# @lc code=end
Solution().merge([[2,6],[8,10],[1,3],[15,18]])
