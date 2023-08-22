#
# @lc app=leetcode id=368 lang=python
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def isDivisible(num1, num2):
            return num1 % num2 == 0 or num2 % num1 == 0
        
        dp = {}
        def rec(index1, index2):

            if (index1, index2) in dp:
                return dp[(index1, index2)]

            if index1 == n:
                return []

            # not select 
            nSelect = [] + rec(index1+1, index2)

            # select
            select = []
            if index2 == -1 or isDivisible(nums[index1], nums[index2]):
                select = [nums[index1]] + rec(index1+1, index1) 

            dp[(index1, index2)] = select if len(select) > len(nSelect) else nSelect
            return dp[(index1, index2)]
        
        nums.sort()
        n = len(nums)
        # return rec(0, -1)

        dp = [[[]]*(n+1) for _ in range(n+1)]
        
        for index1 in range(n-1, -1, -1):
            for index2 in range(index1, -1-1, -1):

                nSelect = [] + dp[index1+1][index2+1]

                # select
                select = []
                if index2 == -1 or isDivisible(nums[index1], nums[index2]):
                    select = [nums[index1]] + dp[index1+1][index1+1] 

                dp[index1][index2+1] = select if len(select) > len(nSelect) else nSelect

        return dp[0][0]



        
# @lc code=end
# print(Solution().largestDivisibleSubset([1,2,3]))
# print(Solution().largestDivisibleSubset([1,2,4,8]))
print(Solution().largestDivisibleSubset(sorted([5,9,18,54,108,540,90,180,360,720])))
# print(Solution().largestDivisibleSubset([108,540,180]))

