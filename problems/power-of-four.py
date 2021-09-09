# https://leetcode.com/problems/power-of-four

# Not the fastest. TODO: Explore other solution approaches

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        4**0 = 1 = 0000000001
        4**1 = (2**2)**1 = 4 = 0000000100
        4**2 = (2**2)**2 = 16 = 000010000 
        4**3 = (2**2)**3 = 64 = 001000000 
        etc.

        So, 
        n > 0
        bin(n) has exactly one 1-bit
        it's at position last, last-2, last-4

        """
    
        if n < 1:
            return False

        s = bin(n)[2:]

        # latter condition check that the only 1 bit is at right position
        return s.count("1") == 1 and (s.index("1") + len(s)) % 2 != 0

        # another neat approach
            # Is positive
            # Is power of 2
            # has the only 1-bit at the odd position
            #return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num  
