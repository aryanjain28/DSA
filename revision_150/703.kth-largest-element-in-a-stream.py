#
# @lc app=leetcode id=703 lang=python
#
# [703] Kth Largest Element in a Stream
#

import heapq

# @lc code=start
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end



n = [4,5,2,45,54,6,7,4,82,2,2,52,1,23,1,42,5,45,3456,656,56]
heapq.heapify(n)

while n:
    print(heapq.heappop(n))