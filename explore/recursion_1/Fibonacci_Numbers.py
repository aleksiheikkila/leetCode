# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.memoize(n)
    
    def memoize(self, n: int):
        # bottom up
        cache = {0: 0, 1: 1}
        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]
            
        return cache[n]
    
# TODO: Decorator approach!


    def fib_iter(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        
        curr = 0
        prev2, prev1 = 1, 1
        
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
            
        return curr
        
        
