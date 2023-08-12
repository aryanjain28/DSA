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

        if len(prices) < 2:
            return 0

        mini = min(prices[0], prices[1])
        prices[0] = 0
        index = 1

        while index < len(prices):
            mini = min(mini, prices[index])
            prices[index] = max(prices[index-1], prices[index]-mini)

            index += 1

        return prices[-1]
        


        
# @lc code=end

