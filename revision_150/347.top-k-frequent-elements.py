#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

from collections import Counter
import heapq
# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # freq = Counter(nums)

        # heap = []
        # for (k, v) in freq.items():
        #     heapq.heappush(heap, (v, k))

        # return [p for (_, p) in heapq.nlargest(K, heap)]

        
        return [x for x, _ in sorted(Counter(nums).items(), key=lambda p: p[1], reverse=True)[:K]]


        # heappush(heap, (1, nums[0]))

        # currCount = 1
        # index = 1
        # while index < len(nums):
        #     if nums[index-1] == nums[index]:
        #         currCount += 1
        #     else:
        #         currCount = 1

        #     heappush(heap, (currCount, nums[index]))
        #     index += 1


        # return [x for (_, x) in heapq.nlargest(k, heap)]




        
# @lc code=end
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))
print(Solution().topKFrequent([3,0, 1,0], 1))