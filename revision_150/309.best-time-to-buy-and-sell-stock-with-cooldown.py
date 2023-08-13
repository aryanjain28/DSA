#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # dp = {}
        # def rec(index, canBuy):

        #     if (index, canBuy) in dp:
        #         return dp[(index, canBuy)]

        #     if index >= n:
        #         return 0
            
        #     if index == n-1:
        #         if canBuy:
        #             return 0
        #         return prices[index]
            

        #     if canBuy:
                
        #         buy = -prices[index] + rec(index+1, not canBuy)
        #         not_buy = 0 + rec(index+1, canBuy)
        #         dp[(index, canBuy)] = max(buy, not_buy)
            
        #     else:
                
        #         sell = prices[index] + rec(index+2, not canBuy)
        #         not_sell = 0 + rec(index+1, canBuy)
        #         dp[(index, canBuy)] = max(sell, not_sell)

        #     return dp[(index, canBuy)]


        n = len(prices)
        # return rec(0, True)

        # dp = [[0,0] for _ in range(n+1+1)]
        # dp[0] = [prices[0], 0]
        
        # for index in range(n-1, -1, -1):
        #     for canBuy in [0, 1]:

        #         # buy
        #         if canBuy > 0:
                    
        #             buy = -prices[index] + dp[index+1][0]
        #             not_buy = 0 + dp[index+1][1]
        #             dp[index][canBuy] = max(buy, not_buy)
                
        #         else:
                    
        #             sell = prices[index] + dp[index+2][1]
        #             not_sell = 0 + dp[index+1][0]
        #             dp[index][canBuy] = max(sell, not_sell)

        
        # return dp[0][-1]


        prev2 = [0,0]
        prev = [0,0]
        curr = [0,0]
        
        for index in range(n-1, -1, -1):
            for canBuy in [0, 1]:

                # buy
                if canBuy > 0:
                    
                    buy = -prices[index] + prev[0]
                    not_buy = 0 + prev[1]
                    curr[canBuy] = max(buy, not_buy)
                
                else:
                    
                    sell = prices[index] + prev2[1]
                    not_sell = 0 + prev[0]
                    curr[canBuy] = max(sell, not_sell)

            prev2 = [p for p in prev]
            prev = [c for c in curr]

        return curr[-1]




        
# @lc code=end
print(Solution().maxProfit([1,2,3,0,2]))
print(Solution().maxProfit([0]))