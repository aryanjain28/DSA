#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)
        count = 0
        s = 0

        freq = { 0: 1 }

        for n in nums:
            s += n
            
            if (s - k) in freq:
                count += freq[s-k]

            freq[s] = freq.get(s, 0) + 1


        return count
            

        
# @lc code=end

print(Solution().subarraySum([1,2,3], 3))
print(Solution().subarraySum([1,1,1], 1))