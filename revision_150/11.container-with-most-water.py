#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maximum = 0
        i = 0
        j = len(height) - 1
        while i < j:
            
            area = (j-i) * min(height[i], height[j]) 
            maximum = area if area > maximum else maximum

            # if height[i+1] - height[i] < height[j-1] - height[j]:
            if height[i] >  height[j]:
                j -= 1
            else:
                i += 1

        print(maximum)
        return maximum
            
        
# @lc code=end
Solution().maxArea([1,8,6,2,5,4,8,3,7])
Solution().maxArea([1,8,6,2,5,4,8,25,7])
Solution().maxArea([1,1])

