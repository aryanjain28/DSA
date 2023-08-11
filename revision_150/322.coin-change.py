#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """


        # dp = {}
        # def rec(index, capacity):

        #     if (index, capacity) in dp:
        #         return dp[(index, capacity)]

        #     if capacity == 0:
        #         return 0

        #     if index == 0:
        #         if capacity % coins[index] != 0:
        #             return float("inf")
        #         return capacity // coins[index]

        #     nSelect = rec(index-1, capacity)
        #     select = float("inf")
        #     if capacity >= coins[index]:
        #         select = 1 + rec(index, capacity-coins[index])
            
        #     dp[(index, capacity)] = min(select, nSelect)
        #     return dp[(index, capacity)]

        n = len(coins)
        # res = rec(n-1, amount)
        # return  -1 if res >= float("inf") else res

        if amount == 0:
            return 0


        prev = [float("inf") if n % coins[0] != 0 else n // coins[0] for n in range(amount+1)]
        curr = [p for p in prev]

        for index in range(1, n+1):
            for capacity in range(1, amount+1):
                nSelect = prev[capacity]
                select = float("inf")
                if capacity >= coins[index-1]:
                    select = 1 + curr[capacity-coins[index-1]]

                curr[capacity] = min(select, nSelect)
            
            prev = [c for c in curr]

        return -1 if curr[-1] >= float("inf") else curr[-1]


        

        
# @lc code=end
# Solution().coinChange([1,2,5], 11)
# Solution().coinChange([2], 1)
Solution().coinChange([2], 3)
