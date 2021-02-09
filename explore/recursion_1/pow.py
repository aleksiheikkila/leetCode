class Solution:   
    def myPow(self, x: float, n: int) -> float:
        # it is better to play with the exponentation...
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1./x
        
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x * self.myPow(x*x, n//2)


    def myPow_crappy(self, x: float, n: int) -> float:
        # iterative, naive, extremely slow. Never use
        if n < 0:
            n = -n
            x = 1./x
        
        rst = 1
        for _ in range(n):
            rst *= x
        
        return rst
    
        