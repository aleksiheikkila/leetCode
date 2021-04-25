# https://leetcode.com/problems/longest-palindromic-substring


class Solution:  
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        maxPal = ""
        
        def _search(s, left, right, maxLen, maxPal):
            # Start from the middle and expand to left and right...
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    maxPal = s[left:right+1]
                left  -= 1
                right += 1
                
            return maxLen, maxPal

        
        for i in range(len(s)):
            # odd length palindrome
            maxLen, maxPal = _search(s, i, i, maxLen, maxPal)
                    
            # even length
            maxLen, maxPal = _search(s, i, i+1, maxLen, maxPal)
            
        return maxPal
                    