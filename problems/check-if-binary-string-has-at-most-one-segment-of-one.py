# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
        
        # after strippin zeros, if only ones, then True
        # return s.strip("0").strip("1") == ""
    

        
    def checkOnesSegment_old(self, s: str) -> bool:
        zeros_seen = False
        
        for c in s[1:]:
            if c == "1" and zeros_seen:
                return False
            elif c == "0":
                zeros_seen = True
 
        return True
         