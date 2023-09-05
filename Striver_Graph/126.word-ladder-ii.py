#
# @lc app=leetcode id=126 lang=python
#
# [126] Word Ladder II
#

# @lc code=start
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        wordList = set(wordList)

        if endWord not in wordList: return []

        res = []
        def similarWords(words):

            if len(res) > 0 and len(res[-1]) == len(words):
                return

            last_word = words[-1]
            for index in range(len(last_word)):
                for i in range(ord("a"), ord("a")+26):
                    w = last_word[:index] + chr(i) + last_word[index+1:]
                    if w in wordList: 
                        if w != last_word:
                            q.append(words + [w])
                        if w == endWord:
                            res.append(words + [w])

            if last_word in wordList: wordList.remove(last_word)
            
        q = [[beginWord]]

        
        while q:
            words = q.pop(0)
            if words[-1] == endWord:
                break
            similarWords(words)

        # for r in res:
        #     print(r)

        return res

        
# @lc code=end

# Solution().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
Solution().findLadders("bat", "coz", ["pat","pot","poz","coz","bot"])