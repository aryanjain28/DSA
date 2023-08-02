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

        LEN = len(candidates)
        res = []

        def dfs(index, s, curr):

            if s >= target:
                if s > target:
                    return  
                res.append(curr)
                return
            

            if index >= LEN:
                return
            





            
            # left: select
            dfs(index + 1, s+candidates[index], curr + [candidates[index]])

            # right: not-select
            while index < LEN-1 and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index + 1, s, curr)
            

            return
        
        candidates.sort()
        dfs(0, 0, [])
        return res
        
# @lc code=end
Solution().combinationSum2([1,2,2,2,5], 5)

