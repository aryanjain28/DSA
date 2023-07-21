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
        minimum = prices[0]

        for n in prices[1:]:
            minimum = n if n < minimum else minimum
            max_profit = n-minimum if n-minimum > max_profit else max_profit
        return max_profit

        
# @lc code=end

