# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # return only the integer part
        # Division, multiplication, mod operator not allowed --> BIT MANIPULATION
        
        # << shift bits to left by one == multiply by 2
        # >> shift bits to right by one == divide by 2  (returns int part)
        # so 9 >> 1 == 4
        
        # Negative numbers: two's complement
        # it's one's complement (i.e. ~num, where we flip all bits) + 1
        # When first, leftmost, most significant bit = 1 --> it's negative number
        
        if divisor == 0:
            raise ValueError("Cannot divide by zero!")
        
        isNeg = False
        if (dividend < 0 and divisor > 0) or \
        (dividend > 0 and divisor < 0):
            isNeg = True
            
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        
        while dividend >= divisor:         
            dividend_consumed = divisor
            quotient = 1
            
            while dividend_consumed <= dividend:
                # smallest quotient of multiple of 2 that fulfills:
                # divisor * quotient > dividend
                dividend_consumed <<= 1  # * 2
                quotient <<= 1
            
            # went over, so back one step (divide by 2)     
            dividend -= dividend_consumed >> 1
            ans += quotient >> 1
            
        if isNeg:
            # multip by -1 not allowed --> two's complement
            # ~177 = -178... ~num + 1 == -num
            return ~ans + 1
        elif ans >= 2**31:  # overflow case... so only for positive?
            return 2**31 - 1 
        else:
            return ans
        