#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # res = {}
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 s_triplet = sorted([nums[i], nums[j], nums[k]])
        #                 s = ""
        #                 for t in s_triplet:
        #                     s += str(t)
        #                 res[s] = s_triplet

        # return res.values()


        # nums.sort()
        # triplets = []
        # for i in range(len(nums)-2):
        #     mSet = set()
        #     for j in range(i+1, len(nums)):
        #         if -(nums[i] + nums[j]) in mSet:
        #             triplets.append([nums[i], nums[j], -(nums[i] + nums[j])])                
        #         mSet.add(nums[j])

        # return set([tuple(t) for t in triplets])        
        # # return triplets.values()

        triplets = []

        # most optimized
        nums.sort()
        i = 0
        j = i + 1
        k = len(nums)-1
        
        while i < j < k:
            j = i + 1
            
            curr = nums[i] + nums[j] + nums[k]

            if curr < 0 :
                while j < k and nums[j+1] == nums[j]:
                    j += 1
                j += 1
            elif curr > 0:
                while k > j and nums[k-1] == nums[k]:
                    k -= 1
                k -= 1
            else:
                triplets.append([nums[i], nums[j], nums[k]])
                while i+1 < len(nums)-1 and nums[i+1] == nums[i]:
                    i += 1
                while k-1 > 2 and nums[k-1] == nums[k]:
                    k -= 1
            






        
# @lc code=end
Solution().threeSum([-1,0,1,2,-1,-4])
