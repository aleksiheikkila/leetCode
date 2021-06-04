# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sz = 0
        for c in s.strip()[::-1]:
            if c == " ":
                break
            sz += 1
                
        return sz
            