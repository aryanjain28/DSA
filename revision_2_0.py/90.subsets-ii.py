
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

        res = [] 
        def rec(index, curr):
            if index >= len(nums):
                if index == len(nums): res.append(curr)
                return 


            rec(index+1, curr + [nums[index]])
            
            
            index += 1
            while index < len(nums) and nums[index] == nums[index-1]: 
                index += 1

            rec(index, curr)
                    
    



        nums.sort()    
        rec(0, [])        
        return res





        
# @lc code=end

Solution().subsetsWithDup([1,2,2])