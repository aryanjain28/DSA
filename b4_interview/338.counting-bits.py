#
# @lc app=leetcode id=338 lang=python
#
# [338] Counting Bits
#

# @lc code=start
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n+1)

        for i in range(1, n+1):
            res[i] = res[i // 2] + (0 if i % 2 == 0 else 1)

        return res
        
        # n.log(n)

        

        # counts = []
        # for n in range(N+1):
        #     count = 0
        #     while n != 0:
        #         if n % 2 == 1:
        #             count += 1
        #         n //= 2

        #     counts.append(count)

        # return counts
    
# @lc code=end
print(Solution().countBits(5))
