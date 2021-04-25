# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/982/

class Solution:
    def myPow_crappy(self, x: float, n: int) -> float:
        # iterative, naive, extremely slow! Never do it like this
        if n < 0:
            n = -n
            x = 1./x
        
        rst = 1
        for _ in range(n):
            rst *= x
        
        return rst
    
    
    def myPow(self, x: float, n: int) -> float:
        # it is better to play with the exponentation...
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1./x
        
        if n % 2 == 0:
            return self.myPow(x*x, n/2)  # e.g. 2^4 = 16 == (2*2)^2 = 4^2 = 16
        else:
            return x * self.myPow(x*x, n//2)
        