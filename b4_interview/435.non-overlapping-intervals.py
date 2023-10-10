#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort()
        def isOverlapping(s1, e1, s2, e2):
            if s1 < s2 < e1:
                return True
            elif s1 < e2 < e1:
                return True
            elif s2 < e1 < e2:
                return True
            elif s2 < s1 < e2:
                return True
            elif s1 == s1 and e1 == e2:
                return True
            else:
                return False

        count = 0
        index = 1
        while index < len(intervals):
            
            s1, e1 = intervals[index-1][0], intervals[index-1][1]
            s2, e2 = intervals[index][0], intervals[index][1] 
            
            
            if isOverlapping(s1, e1, s2, e2):
                if e1 < e2:
                    intervals[index] = intervals[index-1]
                    
                count += 1


            index += 1

        return count


        
# @lc code=end
print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
