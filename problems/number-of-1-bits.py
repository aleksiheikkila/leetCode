# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        setbits = 0
        while n > 0:
            n, mod = divmod(n, 2)
            setbits += mod
            
        return setbits
        