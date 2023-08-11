#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp = {}
        def rec(index, target):
            
            if (index, target) in dp:
                return dp[(index, target)]
            
            if target == 0:
                return 1
            
            if index < 0:
                return 0
            
            not_select = rec(index-1, target)
            select = 0
            if target-coins[index] >= 0:
                select = rec(index, target-coins[index])
            
            dp[(index, target)] = select + not_select
            return dp[(index, target)]

        n = len(coins)
        # return rec(n-1, amount)

        prev = [0] * (amount+1)
        prev[0] = 1
        curr = [p for p in prev]

        for index in range(1, n+1):
            curr[0] = 1
            for target in range(1, amount+1):

                not_select = prev[target]
                select = 0
                if target-coins[index-1] >= 0:
                    select = curr[target-coins[index-1]]
                
                curr[target] = select + not_select
            
            prev = [c for c in curr]

        return curr[-1]


        
# @lc code=end
print(Solution().change(5, [1,2,5]))
print(Solution().change(3, [2]))
print(Solution().change(10, [10]))
