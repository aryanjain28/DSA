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

        max_profit = 0
        mini = prices[0]
        for n in prices[1:]:
            mini = min(mini, n)
            max_profit = max(max_profit, n - mini)

        return max_profit

        
# @lc code=end

