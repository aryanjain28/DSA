#
# @lc app=leetcode id=211 lang=python
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(node, word):

            if not word:
                return node.word

            if word[0] == ".":
                for n in node.children.values():
                    if dfs(n, word[1:]):
                        return True
                return False

            elif word[0] not in node.children:
                return False

            return dfs(node.children[word[0]], word[1:])
        
        return dfs(self.root, word)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

wd = WordDictionary()
wd.addWord("b")
print(wd.search(".."))

