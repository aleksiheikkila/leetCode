# https://leetcode.com/problems/replace-words

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}  # defaultdict(list)  # 
        

class Trie:
    def __init__(self):
        self.root = TrieNode("")
        
        
    def add(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                newNode = TrieNode(c)
                node.children[c] = newNode
                node = newNode
                
        node.is_end = True
            
            
    def find_shortest_word(self, search_word):
        """Returns the shortest prefix of the search_word
        e.g. battery --> bat
        """
        node = self.root
        
        for i, c in enumerate(search_word):
            if c in node.children:
                node = node.children[c]
                if node.is_end:
                    return search_word[:i+1]
            else:
                return None
        
        return search_word if node.is_end else None
        


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """Using Trie"""
        roots = []
        
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        
        for word in sentence.split():
            shortest_base_in_dict = trie.find_shortest_word(word)
            if shortest_base_in_dict is not None:
                roots.append(shortest_base_in_dict)
            else:
                roots.append(word)
            
        return " ".join(roots)
    
    
    def replaceWords_old(self, dictionary: List[str], sentence: str) -> str:
        from collections import defaultdict
        
        roots = []
        
        # should use more complete trie, for faster lookup?
        # Now just splitting by first char...
        
        d =  defaultdict(list)
        
        for w in dictionary:
            d[w[0]].append(w)  # "a": ["apple", "animal", ...]
            
        for word in sentence.split():
            dict_words = d[word[0]]
            a = word
            for i in range(1, len(word)):
                if word[:i] in dict_words:
                    #print("found", word[:i])
                    a = word[:i]
                    #roots.append(word[:i])
                    break
                    
            roots.append(a)
            
        return " ".join(roots)