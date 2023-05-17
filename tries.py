# Also called, prefix trees.
# Tries have tree like structure. 
# These were basically built for storing and searching strings.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True
        return self.root
    
    def search(self, word) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word
    
    def startsWith(self, prefix) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
    

        
    