# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3728/

# Trie

import collections

Trie = lambda: collections.defaultdict(Trie)
# t=Trie() dict with empty dict as the default value... and so on

class WordFilter:
    # hashmap based
    def __init__(self, words: List[str]):
        self.lookup = {}
        # key is the (prefix, suffix). Value is the (largest) index of a matching word
        # Takes quite a bit memory...
        
        for idx, word in enumerate(words):
            N = len(word)
            
            for i in range(1, N+1):
                for j in range(0, N):
                    self.lookup[(word[:i], word[j:])] = idx  # in the end, has the largest index....
            
                    
    def f(self, prefix: str, suffix: str) -> int:
        return self.lookup.get((prefix, suffix), -1) 



    # Trie based
    def __init2__(self, words: List[str]):
        self.trie = Trie()
        
        for weight, word in enumerate(words):
            for i in range(len(word) + 1):
                node = self.trie  # start from the top
                node["weight"] = weight
                word_to_insert = word[i:] + "#" + word
                for c in word_to_insert:
                    node = node[c]  # dict
                    node["weight"] = weight
        

    def f2(self, prefix: str, suffix: str) -> int:
        node = self.trie
        for c in suffix + "#" + prefix:
            if c not in node: return -1
            node = node[c]
        return node["weight"]
        
    
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
