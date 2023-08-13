#
# @lc app=leetcode id=188 lang=python
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        dp = {}
        def rec(index, canBuy):
            
            if (index, canBuy) in dp:
                return dp[(index, canBuy)]
            
            if index == n-1:
                # buy
                if canBuy % 2 == 0:
                    return 0
                return prices[index]

            
            if canBuy >= k * 2:
                return 0
            

            # buy
            if canBuy % 2 == 0:
                
                buy = -prices[index] + rec(index+1, canBuy+1)
                not_buy = 0 + rec(index+1, canBuy)
                dp[(index, canBuy)] = max(buy, not_buy)
                
            # sell
            else:
                
                sell = prices[index] + rec(index+1, canBuy+1)
                not_sell = 0 + rec(index+1, canBuy)
                dp[(index, canBuy)] = max(sell, not_sell)
                
            return dp[(index, canBuy)]

        n = len(prices)
        if k > n // 2:
            k = n // 2

        # return rec(0, 0)

        # dp = [[0] * ((k*2)+1) for _ in range(n+1)]
        # dp[0] = [prices[0] if i % 2 != 0 else 0 for i in range(k*2+1)]

        # for index in range(n-1, -1, -1):
        #     for canBuy in range(k*2):
                
        #         # buy
        #         if canBuy % 2 == 0:
                
        #             buy = -prices[index] + dp[index+1][canBuy+1]
        #             not_buy = 0 + dp[index+1][canBuy]
        #             dp[index][canBuy] = max(buy, not_buy)
                    
        #         # sell
        #         else:
                    
        #             sell = prices[index] + dp[index+1][canBuy+1]
        #             not_sell = 0 + dp[index+1][canBuy]
        #             dp[index][canBuy] = max(sell, not_sell)
                    
        # return dp[0][0] 

        dp = [[0] * ((k*2)+1) for _ in range(n+1)]
        dp[0] = [prices[0] if i % 2 != 0 else 0 for i in range(k*2+1)]

        prev = [0] * ((k*2)+1)
        curr = [p for p in prev]

        for index in range(n-1, -1, -1):
            for canBuy in range(k*2):
                
                take = (-1 if canBuy % 2 == 0 else 1) * prices[index] + prev[canBuy+1]
                not_take = 0 + prev[canBuy]
                curr[canBuy] = max(take, not_take)

            prev = [c for c in curr]


        return curr[0]



        
# @lc code=end
print(Solution().maxProfit(2, [2, 4, 1]))
print(Solution().maxProfit(2, [3,2,6,5,0,3]))
print(Solution().maxProfit(2, [3,3,5,0,0,3,1,4]))


