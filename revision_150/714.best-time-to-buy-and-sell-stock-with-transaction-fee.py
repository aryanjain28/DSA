#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        # dp = {}
        # def rec(index: int, canBuy: int):

        #     if (index, canBuy) in dp:
        #         return dp[(index, canBuy)]

        #     if index == n-1:
        #         if canBuy > 0:
        #             return 0
        #         return prices[index]-fee
            
            
        #     # buy
        #     if canBuy > 0:
            
        #         buy = -prices[index] + rec(index+1, 0)
        #         not_buy = 0 + rec(index+1, 1)
        #         dp[(index, canBuy)] = max(buy, not_buy)
            
        #     # sell
        #     else:
                
        #         sell = prices[index] + rec(index+1, 1) - fee
        #         not_sell = 0 + rec(index+1, 0)
        #         dp[(index, canBuy)] = max(sell, not_sell)
            
        #     return dp[(index, canBuy)]

        n = len(prices)
        # return rec(0, 1)

        # dp = [[0, 0] for _ in range(n+1)]
        # dp[0] = [prices[0]-fee, 0]

        # for index in range(n-1, -1, -1):
        #     for canBuy in [0,1]:

        #         # buy
        #         if canBuy == 1:
                
        #             buy = -prices[index] + dp[index+1][0]
        #             not_buy = 0 + dp[index+1][1]
        #             dp[index][canBuy] = max(buy, not_buy)
                
        #         # sell
        #         else:
                    
        #             sell = prices[index] + dp[index+1][1] - fee
        #             not_sell = 0 + dp[index+1][0]
        #             dp[index][canBuy] = max(sell, not_sell)

        # return dp[0][-1]


        prev = [0,0]
        curr = [0,0]

        for index in range(n-1, -1, -1):
            for canBuy in [0,1]:

                # buy
                if canBuy == 1:
                
                    buy = -prices[index] + prev[0]
                    not_buy = 0 + prev[1]
                    curr[canBuy] = max(buy, not_buy)
                
                # sell
                else:
                    
                    sell = prices[index] + prev[1] - fee
                    not_sell = 0 + prev[0]
                    curr[canBuy] = max(sell, not_sell)

            prev = [c for c in curr]

        return curr[-1]


        





        
# @lc code=end
print(Solution().maxProfit([1,3,2,8,4,9], 2))
print(Solution().maxProfit([1,3,7,5,10,3], 3))
