# https://leetcode.com/problems/longest-happy-string

from collections import Counter

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = []
        
        counts = Counter({'a':a,'b':b,'c':c})
        
        prev_char = "n"
        
        for _ in range(a+b+c):
            top2 = counts.most_common(2)
            if top2[0][0] != prev_char:
                char, num = top2[0]
            else:
                char, num = top2[1]
                # if top1 is still larger, need to conserve the second most common char
                if top2[0][1] - top2[1][1] > 0:
                    num = min(num, 1)
                       
            if num == 0:
                break
            
            num_chars_consumed = min(num, 2)
            chars.extend([char] * num_chars_consumed)
            counts[char] -= num_chars_consumed
            prev_char = char
        
        return "".join(chars)
