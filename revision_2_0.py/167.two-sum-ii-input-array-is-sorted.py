#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers)-1

        while i < j:
            
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [i+1, j+1]


            
        

        
# @lc code=end
print(Solution().twoSum([2,5,6,7,8], 7))

