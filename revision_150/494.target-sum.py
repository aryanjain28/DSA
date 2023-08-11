#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, arr, d):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        zero_count = 0
        nums = []
        for num in arr:
            if num == 0:
                zero_count += 1
                continue
            nums.append(num)

        
        d = abs(d)
        total = sum(nums)
        if (total + d) % 2:
            return 0
        
        n = len(nums)
        s = (total + d) // 2

        dp = {}
        def rec(index, target):
            
            if (index, target) in dp:
                return dp[(index, target)]
            
            if target == 0:
                return 1
            
            if index < 0:
                return 0
            
            nSelect = rec(index-1, target)
            select = 0
            if target >= nums[index]:
                select = rec(index-1, target-nums[index])

            dp[(index, target)] = nSelect + select
            return dp[(index, target)]
        
        # return rec(n-1, s) * (2**(zero_count))

        prev = [0] * (s+1)
        prev[0] = 1
        curr = [p for p in prev]

        for index in range(1, n+1):
            curr[0] = 1
            for target in range(1, s+1):
                
                nSelect = prev[target]
                select = 0
                if target >= nums[index-1]:
                    select = prev[target-nums[index-1]]

                curr[target] = select + nSelect

            prev = [c for c in curr]

        return curr[-1] * (2**zero_count)



        
# @lc code=end
# print(Solution().findTargetSumWays([1], -1))
# print(Solution().findTargetSumWays([1, 2], 4))
# print(Solution().findTargetSumWays([2, 2], 4))
# print(Solution().findTargetSumWays([1,1,1,1,1], 3))
# print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
print(Solution().findTargetSumWays([100], -200))
