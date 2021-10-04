# https://leetcode.com/problems/verifying-an-alien-dictionary

from functools import cmp_to_key  # in python3 we need this

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_d = {c: i for i, c in enumerate(order)}
        
        def compare(item1, item2, ord_d=ord_d):
            if item1 == item2:
                return 0
            
            for c1, c2 in zip(item1, item2):
                if ord_d[c1] < ord_d[c2]:
                    return -1
                if ord_d[c1] > ord_d[c2]:
                    return 1
                
            if len(item1) > len(item2):
                return 1
            else:
                return -1
            
            
        return words == sorted(words, key=cmp_to_key(compare))
            