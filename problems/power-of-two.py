# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo_wrong(self, n: int) -> bool:   
        from math import log
        
        if n < 1:
            return False
        x = log(n, 2)
        
        # This doesnt work due to numerical imprecision
        return x == int(x)
        
        
    def isPowerOfTwo(self, n: int) -> bool:  
        """What does it mean that the number is a power of two.
        In binary, it means that there is only one bit with value 1
        
        For positive nbrs
        000001 = 1
        000010 = 2
        000100 = 4
        001000 = 8
        010000 = 16
        100000 = 32
        etc
        """
        
        if n < 1:
            return False
        
        # bin(n) gives the binary representation as str
        return bin(n).count("1") == 1
    

        # Another idea
        # Let's say num = 44 <=> '0b101100' 
        # if we take bitwise and: num & (num-1)
        # '0b101100' & '0b101011'  = '0b101000'
        # n&(n-1) flips the rightmost 1-bit to zero
        # So if n&(n-1) == 0, there was only one 1-bit to begin with!