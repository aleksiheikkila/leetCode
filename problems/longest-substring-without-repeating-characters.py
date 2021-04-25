# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        left = right = 0 
        chars_seen = set()
        
        while right < len(s):
            next_char = s[right]
            if next_char not in chars_seen:
                chars_seen.add(next_char)
                right += 1
            else:
                # seen already... check if new max and advance left side
                if right - left > max_len:
                    max_len = right - left
                while s[left] != next_char:  # go until we have the 1st occurence
                    chars_seen.remove(s[left])
                    left += 1
                    
                left += 1  # go one past, i.e. remove the 1st occurence
                right += 1 # also continue
        
        # in the end, check if we have a new maxlen "in the buffer"
        if right - left > max_len:
            max_len = right - left
                        
        return max_len
        