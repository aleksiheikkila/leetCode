# https://leetcode.com/problems/longest-palindromic-subsequence

# Dynamic programming

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # dynamic programming
        
        # lps = Longest Palindrome Subsequence
        
        # lps(i, j) = LPS for the substring starting at index i, ending at j (inclusive)
        # then
        # lps(x,x) = 1
        # if s[i] == s[j] --> lps(i,j) = lps(i+1, j-1) + 2
        # if not --> lps(i,j) = max(lps(i+1, j), lps(i, j-1))
        # edge case when substr len = 2: if same chars, lps=2, else=1
 
        # matrix of lps[i][j]
        lps = [[0]*len(s) for _ in range(len(s))]  
        
        for i in range(len(s)):
            lps[i][i] = 1
        
        # then start at substring length 2 and fill the upper triangle part
        # going diagonally
        for substr_len in range(2, len(s) + 1):
            for i in range(len(s) - substr_len + 1):
                j = i + substr_len - 1
                  
                if s[i] == s[j]:
                    if j-i == 1:
                        lps[i][j] = 2
                    else:
                        lps[i][j] = 2 + lps[i+1][j-1]
       
                else:
                    lps[i][j] = max(lps[i+1][j], lps[i][j-1])
                
        return lps[0][len(s) - 1]
                    
        