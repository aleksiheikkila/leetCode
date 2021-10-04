# https://leetcode.com/problems/ransom-note

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_chars = Counter(magazine)  # might waste with long magazine and short note
        needed_chars = Counter(ransomNote)
        
        for c, need in needed_chars.items():
            if available_chars[c] < need:
                return False
            
        return True
        

        # Shorter way
        return not Counter(ransomNote) - Counter(magazine)