#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        while n:
            if n & 1: 
                count += 1
            n = n >> 1

        return count

        
# @lc code=end

