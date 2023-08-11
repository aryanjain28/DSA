#
# @lc app=leetcode id=2035 lang=python
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

# @lc code=start
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        total = sum(nums)
        target = total // 2

        def rec(index, limit):

            if limit == 0:
                return nums[index]

            if index < 0:
                return float("inf")
            

            # select
            select = nums[index] + rec(index-1, limit-1)
            # not select
            nSelect = nums[index] + rec(index-1, limit)

            print(nums[index])
            print("Not Select: ", nSelect)
            print("Select: ", select)
            


            diff1 = abs(target-nSelect)
            diff2 = abs(target-select)


            print(nSelect if diff1 < diff2 else select)
            print()


            return nSelect if diff1 < diff2 else select
            
            

            

        mini = rec(n-1, n // 2)
        return abs((mini*2)-total)



        
# @lc code=end
print(Solution().minimumDifference([3, 9, 7, 3]))
