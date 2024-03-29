# https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        
        counts = Counter(s)
        
        for idx, c in enumerate(s):
            if counts[c] == 1:
                return idx
            
        return -1
        