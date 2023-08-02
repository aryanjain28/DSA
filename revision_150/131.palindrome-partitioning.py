#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def isPalindrome(words):
            for word in words:
                if word != word[::-1]:
                    return False
            return True


        LEN = len(s)

        res = []
        def dfs(index, curr):

            if index == LEN:
                res.append(curr)
                return

            # right : add c to curr  
            dfs(index + 1, curr + [s[index]])

            # left : combine with last
            curr[-1] += s[index]
            dfs(index + 1, curr)


        dfs(1, [s[0]])
        # print(res)
        # print([r for r in res if isPalindrome(r)])
        return [r for r in res if isPalindrome(r)]



        
# @lc code=end
Solution().partition("a")

