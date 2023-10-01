#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        mini = prices[0]
        maxi = 0

        for n in prices:
            if n < mini:
                mini = n
            elif n - mini > maxi:
                maxi = n - mini

        return maxi



        
# @lc code=end

