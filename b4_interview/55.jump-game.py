#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        # # dp = [False] * n
        # # index = n - 2
        # # while index > 0:

        # #     dp[index] = dp[index+1] or dp[min(n-1, index + nums[index])]
        # #     index -= 1

        # # print(dp)

        # # if nums.count(0) == 0:
        # #     return True

        # # n = len(nums)

        # # dp = {}
        # # def dfs(index):

        # #     if index in dp:
        # #         return dp[index]

        # #     if index == n-1:
        # #         return True
            
        # #     if index >= n or nums[index] == 0:
        # #         return False
            
        # #     maxi = min(index + nums[index], n-1)
        # #     mini = index + 1

        # #     for i in range(mini, maxi+1):
        # #         if dfs(i):
        # #             dp[index] = True
        # #             return dp[index]
                    
            
        # #     dp[index] = False
        # #     return dp[index]


        # dp = [False] * n
        # dp[-1] = True

        # for index in range(n-1, -1, -1):
            
        #     if nums[index] == 0:
        #         continue
            
        #     maxi = min(index + nums[index], n-1)
        #     mini = index + 1

        #     for i in range(mini, maxi+1):
        #         if dp[i]:
        #             dp[index] = True
        #             break
                    
            
            
            # return dp[index]

        
        # return dp[0]


        # Greedy Solution

        goal = n-1
        index = n-2
        while index >= 0:
            
            if index + nums[index] >= goal:
                goal = index
        
            index -= 1

        return goal == 0


        
# @lc code=end
print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([0]))
print(Solution().canJump([2,0]))
