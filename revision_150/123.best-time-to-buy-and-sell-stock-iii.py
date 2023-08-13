#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        def isEven(m): return (m % 2 == 0)
        
        dp = {}
        def rec(index, canBuy):
            
            if (index, canBuy) in dp:
                return dp[(index, canBuy)]
            
            if index == n-1:
                if not isEven(canBuy):
                    return 0
                return prices[index]
            
            if canBuy > 4:
                return 0

            if not isEven(canBuy):                
                buy = -prices[index] + rec(index+1, canBuy+1)
                not_buy = 0 + rec(index+1, canBuy)
                dp[(index, canBuy)] = max(buy, not_buy)
            else:
                sell = prices[index] + rec(index+1, canBuy+1)
                not_sell = 0 + rec(index+1, canBuy)
                dp[(index, canBuy)] = max(sell, not_sell)

            return dp[(index, canBuy)]

        n = len(prices)
        # return rec(0, 1)

        # dp = [[0]*(4+1) for _ in range(n+1)]
        # dp[0] = [prices[0], 0, prices[0], 0, 0]

        # for index in range(n-1, -1, -1):
        #     for canBuy in range(4):
                
        #         if isEven(canBuy):                
        #             buy = -prices[index] + dp[index+1][canBuy+1]
        #             not_buy = 0 + dp[index+1][canBuy]
        #             dp[index][canBuy] = max(buy, not_buy)
        #         else:
        #             sell = prices[index] + dp[index+1][canBuy+1]
        #             not_sell = 0 + dp[index+1][canBuy]
        #             dp[index][canBuy] = max(sell, not_sell)
                

        # return dp[0][0]


        prev = [0]*(4+1)
        curr = [0]*(4+1)

        for index in range(n-1, -1, -1):
            for canBuy in range(4):
                
                if isEven(canBuy):                
                    buy = -prices[index] + prev[canBuy+1]
                    not_buy = 0 + prev[canBuy]
                    curr[canBuy] = max(buy, not_buy)
                else:
                    sell = prices[index] + prev[canBuy+1]
                    not_sell = 0 + prev[canBuy]
                    curr[canBuy] = max(sell, not_sell)
                
            prev = [c for c in curr]

        return curr[0]
                





        
# @lc code=end
print(Solution().maxProfit([3,5]))
print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))
