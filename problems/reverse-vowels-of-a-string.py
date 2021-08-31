# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    # rather slow
    
    def reverseVowels(self, s: str) -> str:
        VOWELS = ("a", "e", "i", "o", "u")
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left].lower() in VOWELS and chars[right].lower() in VOWELS:
                chars[left], chars[right] = chars[right], chars[left]
                left, right = left + 1, right - 1
            else:
                if s[left].lower() not in VOWELS:
                    left += 1
                if s[right].lower() not in VOWELS:
                    right -= 1
             
        return "".join(chars)
        