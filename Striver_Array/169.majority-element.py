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

        freq = 0
        curr = 0
        for n in nums:
            if freq == 0:
                curr = n
                freq = 1
                continue

            if n == curr:
                freq += 1
            else:
                freq -= 1
            
            
        return curr


        # mMap = {}
        # for n in nums:
        #     mMap[n] = mMap.get(n, 0) + 1
        #     if mMap[n] > len(nums) // 2:
        #         return n


        
# @lc code=end

