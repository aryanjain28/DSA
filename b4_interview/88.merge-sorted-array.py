#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # for i, n in enumerate(sorted(nums1[:m] + nums2)):
        #     nums1[i] = n

        i = m - 1
        j = n - 1
        index = m + n - 1

        while j >= 0:

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1

            index -= 1


        
        
# @lc code=end

Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)