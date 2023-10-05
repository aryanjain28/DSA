#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        maj_1 = 0
        maj_2 = 0
        count_1 = 0
        count_2 = 0

        for n in nums:
            
            if n == maj_1:
                count_1 += 1
            elif n == maj_2:
                count_2 += 1
            elif count_1 == 0:
                count_1 = 1
                maj_1 = n
            elif count_2 == 0:
                count_2 = 1
                maj_2 = n
            else:
                count_1 -= 1
                count_2 -= 1

        res = set()
        LEN = len(nums)

        if nums.count(maj_1) > LEN / 3:
            res.add(maj_1)
        
        if nums.count(maj_2) > LEN / 3:
            res.add(maj_2)

        return res
        



        # res = set()
        # LEN = len(nums)

        # mMap = {}
        # for n in nums:
        #     mMap[n] = mMap.get(n, 0) + 1
        #     if mMap[n] > LEN // 3:
        #         res.add(n)

        #     if len(res) == 2:
        #         return res

        # return res
        
# @lc code=end

