# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        N_t, N_s = len(t), len(s) 
        p1 = p2 = 0
        # p1 points to string t, p2 to string s
        
        while p1 < N_t and p2 < N_s:
            # found next char from required substr:
            if s[p2] == t[p1]:
                p2 += 1    
            p1 += 1
            
        return True if p2 == N_s else False
     