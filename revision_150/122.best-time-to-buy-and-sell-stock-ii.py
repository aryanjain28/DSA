#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)

        # dp = {}

        # def rec(index, canBuy):

        #     if (index, canBuy) in dp:
        #         return dp[(index, canBuy)]
            
        #     if (index == n-1):
        #         if canBuy:
        #             return 0 
        #         return prices[n-1]

        #     if canBuy == 1:
        #         buy_profit = -prices[index] + rec(index+1, 0)
        #         n_buy_profit = 0 + rec(index+1, 1)
        #         dp[(index, canBuy)] = max(buy_profit, n_buy_profit)
        #     else: 
        #         sell_profit = prices[index] + rec(index+1, 1)
        #         n_sell_profit = 0 + rec(index+1, 0)
        #         dp[(index, canBuy)] = max(sell_profit, n_sell_profit)

        #     return dp[(index, canBuy)]

        # # return rec(0, 1)

        # dp = [[0]*2 for _ in range(n+1)]
        # dp[0][0] = prices[0]

        # for index in range(n-1, -1, -1):
        #     for canBuy in range(0, 2):

        #         if canBuy == 1:
        #             buy_profit = -prices[index] + dp[index+1][0]
        #             n_buy_profit = 0 + dp[index+1][1]
        #             dp[index][canBuy] = max(buy_profit, n_buy_profit)
        #         else: 
        #             sell_profit = prices[index] + dp[index+1][1]
        #             n_sell_profit = 0 + dp[index+1][0]
        #             dp[index][canBuy] = max(sell_profit, n_sell_profit)

        # return dp[0][1]
    

        prev = [0, 0]
        curr = [0, 0]
        for index in range(n-1, -1, -1):
            for canBuy in range(0,2):
                
                if canBuy == 1:
                    buy_profit = -prices[index] + prev[0]
                    n_buy_profit = 0 + prev[1]
                    curr[1] = max(buy_profit, n_buy_profit)
                else: 
                    sell_profit = prices[index] + prev[1]
                    n_sell_profit = 0 + prev[0]
                    curr[0] = max(sell_profit, n_sell_profit)
            
            prev = [p for p in curr]

        return curr[1]









        
# @lc code=end
print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit(list(reversed([1,2,3,4,5]))))
print(Solution().maxProfit([1,2,3,4,5]))

