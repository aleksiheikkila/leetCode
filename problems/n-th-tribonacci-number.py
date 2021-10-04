# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        return self.memoize(n)
    
    
    def memoize(self, n):
        cache = {0: 0, 1: 1, 2: 1}
        
        for i in range(3, n + 1):
            cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
            
        return cache[n]
        