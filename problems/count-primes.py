# https://leetcode.com/problems/count-primes

# Count the number of prime numbers less than a non-negative number, n
# (by sieve of eratosthenes)

# Not very fast and consumes a lot of mem

class Solution:
    def countPrimes(self, n: int) -> int:
        # Eratosthene’s method (Sieve)
        if n < 2:
            return 0
        
        isPrime = [True for _ in range(n)]
        p = 2
        
        while p*p <= n:
            # need to go up to sqrt(n)
            
            if isPrime[p]:
                for i in range(p*p, n, p):
                    isPrime[i] = False         
            p += 1
        
        return sum(isPrime[2:])
        