#
# @lc app=leetcode id=1035 lang=python
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        n = len(nums1)
        m = len(nums2)
        matrix = [[0] * (m + 1) for _ in range(n+1)]
        maximum = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums1[i-1] == nums2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                    maximum = maximum if maximum > matrix[i][j] else matrix[i][j]
                else:
                    matrix[i][j] = matrix[i-1][j] if matrix[i-1][j] > matrix[i][j-1] else matrix[i][j-1]


        return maximum
                

# @lc code=end
Solution().maxUncrossedLines([5,1,8], [8,1,5])

