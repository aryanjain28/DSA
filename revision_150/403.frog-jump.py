#
# @lc app=leetcode id=403 lang=python
#
# [403] Frog Jump
#

# @lc code=start
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        n = len(stones)

        if stones[1] != 1:
            return False
        
        # stones = 
        set_stones = set(stones)
        river = set(range(1, stones[-1])).difference(set_stones)
        print(river)
        
        def rec(index, currStep, jumpUnit):

            print(currStep)

            if index >= n or jumpUnit <= 0 or currStep in river:
                return False
            
            if index == n-1 and currStep == stones[-1]:
                return True
            
            

            a = rec(index+1, currStep+jumpUnit-1, jumpUnit-1)
            b = rec(index+1, currStep+jumpUnit, jumpUnit)
            c = rec(index+1, currStep+jumpUnit+1, jumpUnit+1)

            return a or b or c




            
        return rec(0, 0, 1)



        
# @lc code=end
print(Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17]))
