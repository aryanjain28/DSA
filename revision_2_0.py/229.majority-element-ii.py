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

        e1 = None
        e2 = None

        c1 = 0
        c2 = 0

        N = len(nums)

        for n in nums:

            if c1 == 0 and n != e2:
                e1 = n

            elif c2 == 0 and n != e1:
                e2 = n

            if n == e1:
                c1 += 1
            elif n == e2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
                

        c1 = 0
        c2 = 0

        for n in nums:
            if n == e1:
                c1 += 1
            if n == e2:
                c2 += 1


        res = set()

        if c1 > N // 3:
            res.add(e1)

        if c2 > N // 3:
            res.add(e2)

        return res
        

            





        # count = 0
        # res = set()
        # nums.sort()

        # for index, n in enumerate(nums):
        #     if index > 0 and nums[index-1] != n:
        #         count = 0

        #     count += 1

        #     if count > len(nums) // 3:
        #         res.add(n)

        
        # return res

        # count = {}
        # res = set()
        # LEN = len(nums)
    
        # for n in nums:
        #     count[n] = count.get(n, 0) + 1
        #     if count[n] > LEN // 3: res.add(n)

        # return res

        
# @lc code=end
# print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))
# print(Solution().majorityElement([1,2]))
