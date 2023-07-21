#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        res = [0] * len(temperatures)
        mStack = [(temperatures[0], 0)]

        index = 1
        while index < len(temperatures):
            while mStack and mStack[-1][0] < temperatures[index]:
                _, i = mStack.pop()
                res[i] = index - i

            mStack.append((temperatures[index], index))
            index += 1 

        return res

        
# @lc code=end
Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
Solution().dailyTemperatures([30, 60, 90])
Solution().dailyTemperatures([30, 40, 50, 60])
