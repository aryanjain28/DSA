#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        freq = {}
        for index, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in freq:
                return [index, freq[n2]]
            
            freq[n1] = index

        # freq = {}
        # for index, n in enumerate(nums):
        #     freq[n] = freq.get(n, [])
        #     freq[n].append(index)

        # for index, n1 in enumerate(nums):
        #     n2 = target - n1
        
        #     if n2 in freq:
        #         if n1 == n2:
        #             if len(freq[n2]) > 1:
        #                 return freq[n2]
        #             continue

        #         return [index, freq[n2][0]]

        


# @lc code=end
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 7))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))

