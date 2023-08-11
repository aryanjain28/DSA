#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """



        # dp = {}
        # def rec(index, target):
            
        #     if (index, target) in dp:
        #         return dp[(index, target)]

        #     if index < 0 or target < 0:
        #         return False
            
        #     if target == 0: 
        #         return True

        #     # not-select
        #     nSelect = rec(index-1, target)
        #     # select
        #     Select = rec(index-1, target-nums[index])

        #     dp[(index, target)] = Select or nSelect
        #     return dp[(index, target)]
            
        # return rec(n-1, total // 2)

        
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:    
            return False
        

        dp = [[False for _ in range(total+1+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][1] = True

        for index in range(1, n+1):
            for target in range(2, total+2):
                
                nSelect = dp[index-1][target]
                Select = False
                if target >= nums[index-1]:
                    Select = dp[index-1][target-nums[index-1]]

                dp[index][target] = Select or nSelect


        dp = dp[-1][1:]

        mini = float("inf")
        for n, possible in enumerate(dp):
            if possible:
                diff = abs((2 * n) - total)
                mini = mini if mini < diff else diff


        print(mini)
        return ""
        

        
# @lc code=end
print(Solution().canPartition([1,5,11,5]))
print(Solution().canPartition([1,2,3,5]))
print(Solution().canPartition([1,2,5]))

