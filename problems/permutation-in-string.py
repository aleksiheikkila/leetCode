# https://leetcode.com/problems/permutation-in-string

class Solution:    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        ord_a = ord("a")
        
        for c in s1:
            s1_counts[ord(c) - ord_a] += 1 
        
        s2_window_counts = [0] * 26
        for i in range(len(s1)):
            s2_window_counts[ord(s2[i]) - ord_a] += 1
            
        if s2_window_counts == s1_counts:
            return True
        
        # then rolling window. Remove one char from left, add one new to right
        left, right = 0, len(s1)
        while right < len(s2):
            s2_window_counts[ord(s2[left]) - ord_a] -= 1
            s2_window_counts[ord(s2[right]) - ord_a] += 1
            
            if s2_window_counts == s1_counts:
                return True
            
            left += 1
            right += 1
            
        return False


    def checkInclusion_slower(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        # take s2 character counts
        
        # Check len(s2) length substrings in s1
        from collections import Counter
        
        s1_counts = Counter(s1)
        
        for start_idx in range(len(s2) - len(s1) + 1):
            if Counter(s2[start_idx:start_idx+len(s1)]) == s1_counts:
                return True
            
        return False
