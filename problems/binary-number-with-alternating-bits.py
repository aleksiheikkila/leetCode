# https://leetcode.com/problems/binary-number-with-alternating-bits

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Example 1. Alternating
        # n:            10101010101010
        # n >> 1:       01010101010101
        # n ^ (n >> 1)  11111111111111
        # ans & ans+1 = 0
        
        # Example 2. Not alternating
        # n:            10101010101011
        # n >> 1:       01010101010101
        # n ^ (n >> 1)  11111111111110
        # ans & ans+1 > 0
    
        a = n ^ (n >> 1)
        return (a & (a+1)) == 0
        

        # Alternative
        #s = bin(n)
        #return '00' not in s and '11' not in s