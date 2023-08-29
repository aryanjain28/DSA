#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

import math
# @lc code=start

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        maxi = max(piles)
        total = sum(piles)

        i = 1 if total // h <= 0 else math.ceil(total // h)
        j = maxi

        def can_finish(speed):
            hours = 0
            for p in piles:
                hours += (math.ceil(p / speed))
            return hours <= h

        mini = float("inf")
        while i <= j:
            k = (i + j) // 2
            can_finish_all = can_finish(k)

            if can_finish_all:
                mini = min(mini, k)
                j = k - 1
            else:
                i = k + 1
                
        return mini

        


        
# @lc code=end

print(Solution().minEatingSpeed([312884470], 968709470))
# print(Solution().minEatingSpeed([3,6,7,11], 8))
# print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 5))
# print(Solution().minEatingSpeed(piles = [30,11,23,4,20], h = 6))