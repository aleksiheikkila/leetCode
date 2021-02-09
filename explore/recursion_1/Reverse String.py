# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/

# Did not use recursion

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers, swapping
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
            
    
    def reverseString_onePtr(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # similar idea with one explicit pointer
        i = 0
        while i < len(s) / 2:
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
            i += 1
            