#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if sum(candidates) < target:
            return []
        elif sum(candidates) < target:
            return candidates

        candidates.sort()
        n = len(candidates)
        res = []

        dp = {}
        def dfs(index, s, arr):

            if s == target:
                res.append(arr)
                return

            if s > target or index >= n:
                return 
            
            dfs(index + 1, s + candidates[index], arr + [candidates[index]])
            
            # not select
            index += 1
            while index < n and candidates[index] == candidates[index-1]:
                index += 1
            
            
            dfs(index, s, arr)
            

        dfs(0, 0, [])
        return set([tuple(element) for element in res])

        

    
        
# @lc code=end
print(Solution().combinationSum2([3,1,2], 3))
print(Solution().combinationSum2([10,1,2,7,6,1,5], target = 8))
