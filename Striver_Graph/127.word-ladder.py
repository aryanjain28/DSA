#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        wordList = set(wordList)
        q = [(beginWord, 1)]

        

        def similarWords(word, l):
            if word in wordList: wordList.remove(word)
            for index, _ in enumerate(word):
                for i in range(ord('a'), ord('a')+26):
                    w = word[:index] + chr(i) + word[index+1:]
                    if w in wordList:
                        if w == endWord:
                            return True
                        q.append((w, l+1))
                        wordList.remove(w)

            return False



        while q:
            (word, length) = q.pop(0)
            if similarWords(word, length):
                return length + 1
            
        return 0
            





        
# @lc code=end

Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])