# https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr2(self, haystack: str, needle: str) -> int:
        """Directly using str index method"""
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
        
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            for hay_c, needle_c in zip(haystack[i:], needle):
                if hay_c != needle_c:
                    break
            else:
                #The else clause executes after the loop completes normally. 
                # This means that the loop did not encounter a break statement.
                return i
        return -1
                    