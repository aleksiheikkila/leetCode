# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3722/

from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return True if 3 ** round(log(n, 3)) == n else False

# BTW, check the solution 4: https://leetcode.com/problems/power-of-three/solution/
# Neat


    def isPowerOfThree2(self, n: int) -> bool:
        if n <= 0:
            return False
        
        MAXINT = 2**31 - 1  # py 3 has unbounded int, but this is given in the problem statement
        v = 3 ** int(log(MAXINT, 3))  # 3 is a prime, divisible only by 1 and 3
        # Since 3 is a prime number, the only divisors of 3**19 are
        # 3**0, 3**1, ... 3**19
        # if 3**19 % n == 0 
        # --> n is a divisor of 3**19
        # --> n is a power of three
        return True if v % n == 0 else False