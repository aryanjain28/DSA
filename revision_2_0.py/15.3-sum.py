#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        LEN = len(nums)
        if LEN == 3:
            if sum(nums) == 0:
                return [nums]
            return []
        
        nums.sort()
        res = {}
        for p in range(LEN-2):
            if p != 0 and nums[p] == nums[p-1]:
                continue
            mSet = set()
            for q in range(p+1, LEN):
                if -(nums[p] + nums[q]) in mSet:
                    key = "".join(str(s) for s in sorted([nums[p], nums[q], -(nums[p] + nums[q])]))                    
                    res[key] = ([nums[p], nums[q], -(nums[p] + nums[q])])

                mSet.add(nums[q])

        return res.values()








        
# @lc code=end

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 0, 0, 0]))
# print(Solution().threeSum([-2,0,0,2,2]))