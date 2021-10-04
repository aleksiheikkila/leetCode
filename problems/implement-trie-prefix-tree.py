# https://leetcode.com/problems/implement-trie-prefix-tree

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("")


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                newNode = TrieNode(c)
                node.children[c] = newNode
            node = node.children[c]
        node.is_end = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
            
        return True if node.is_end else False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
            
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)