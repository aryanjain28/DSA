#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sorted(nums)[len(nums) // 2]

        # b = 1
        # res = nums[0]

        # for n in nums[1:]:
        #     if b == 0: res = n
        #     b = b + (1 if n == res else -1)

        # return res

# @lc code=end

print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))