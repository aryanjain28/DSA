#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#


from heapq import heappop, heappush, heapify
# @lc code=start
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        heavy_stones = [(-s) for s in stones]
        heapify(heavy_stones)


        while len(heavy_stones) > 1:
            s1, s2 = -heappop(heavy_stones), -heappop(heavy_stones)

            if abs(s1-s2) > 0:
                heappush(heavy_stones, -abs(s1-s2))
            
        if heavy_stones:
            return -heavy_stones[0]
        
        return 0
                


                    
        
# @lc code=end
print(Solution().lastStoneWeight([2,7,4,1,8,1]))
print(Solution().lastStoneWeight([1]))
