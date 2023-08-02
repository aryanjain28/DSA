#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        LEN = len(nums)
        res = []
        def dfs(index, curr):
            if index >= LEN:
                res.append(curr)
                return

            # left: select            
            dfs(index + 1, curr + [nums[index]])


            # right: not select
            index += 1
            while index < LEN and nums[index] == nums[index-1]:
                index += 1
            dfs(index, curr)


            return

        nums.sort()        
        dfs(0, [])
        return res

        
# @lc code=end
Solution().subsetsWithDup([1,2,2, 3])
