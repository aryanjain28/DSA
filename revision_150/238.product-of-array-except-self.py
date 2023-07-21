#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        LEN = len(nums)
        res = [1] * LEN
        index = 1
        while index < LEN:
            res[index] = res[index-1] * nums[index-1]
            index += 1
    
        prod = nums[-1]
        index = LEN - 2
        while index >= 0:
            res[index] = res[index] * prod
            prod *= nums[index]
            index -= 1

        return res





        # l2r = [1]
        # index = 1
        # while index < len(nums):
        #     l2r.append(l2r[index-1] * nums[index-1])
        #     index += 1

        # r2l = [1]
        # index = len(nums) - 2
        # while index >= 0:
        #     r2l = [r2l[0] * nums[index+1]] + r2l
        #     index -= 1

        # return [l2r[i] * r2l[i] for i in range(len(nums))]





        
# @lc code=end
print(Solution().productExceptSelf([1,2,3,4]))

