class Solution:
# Given a non-negative integer x, compute and return the square root of x.
# Return type is an integer, the decimal digits are truncated, 
# and only the integer part of the result is returned.
    def mySqrt(self, x: int) -> int:     
        left = 0
        right = (x // 2) + 1
        sol = -1
        
        while left <= right:
            mid = (left + right) // 2
            squared = mid**2
            
            if squared == x:
                return mid
            elif squared > x: 
                right = mid - 1
            else:
                left = mid + 1
                # solution is the largest int that fits...
                sol = mid
                
        return sol
