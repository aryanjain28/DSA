#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "":
            return []

        mDict = {}

        for n in range(97, 97+26-11):
            d = ((n-97) // 3) + 2
            mDict[d] = mDict.get(d, []) + [chr(n)]
        
        mDict[7] = ["p", "q", "r", "s"]
        mDict[8] = ["t", "u", "v"]
        mDict[9] = ["w", "x", "y", "z"]


        LEN = len(digits)

        res = []
        def dfs(index, curr):

            if index >= LEN:
                res.append(curr)
                return
            
            for c in mDict[int(digits[index])]:
                dfs(index + 1, curr + c)

            
        dfs(0, "")
        return res



# @lc code=end

Solution().letterCombinations("23")