# https://leetcode.com/problems/perfect-squares/

from math import sqrt
class Solution:
    
    def _numSquares_recursive(self, n):
        # base case
        if n <= 3:
            return n
        
        # memo
        #if n in self.subresults:
        #    return self.subresults[n]
        if self.subresults[n] != -1:
            return self.subresults[n]
        
        sqrt_n = int(sqrt(n))
        if sqrt_n ** 2 == n:
            self.subresults[n] = 1
            return 1

        ans = n
        i = 1
        while i*i < n:
            # use i**2, recurse to what is left
            ans = min(ans, 1 + self._numSquares_recursive(n - i*i))
            i += 1
        
        self.subresults[n] = ans
        
        return ans
        
        
    def numSquares(self, n: int) -> int:
        # A perfect square is a number that is generated by multiplying two equal integers by each other. For example, the number 9 is a perfect square because it can be expressed as a product of two equal integers: 9 = 3 x 3.
        
        # ensin isoin mahdollinen perfect square
        
        #self.subresults = {}  # {i:i for i in range(4)}
        self.subresults = [-1 for _ in range(n+1)]
        
        return self._numSquares_recursive(n)
