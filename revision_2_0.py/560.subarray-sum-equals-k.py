#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        dp = {}
        def rec(index, k):
            
            if (index, k) in dp:
                return dp[(index, k)]


            if k == 0:
                return 1
            
            
            if index < 0:
                return 1 if k == 0 else 0
                        





                       
 
            # select
            select = rec(index-1, k-nums[index])

            # not-select
            not_select = rec(index-1, K)

            dp[(index, k)] = select + not_select
            return dp[(index, k)]

        return rec(len(nums)-1, K)


        
# @lc code=end
print(Solution().subarraySum([1,1,1], 2))
print(Solution().subarraySum([1,2,3], 3))
print(Solution().subarraySum([1,2,1,2,1], 3))
