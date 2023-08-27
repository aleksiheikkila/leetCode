""" 
202. Happy Number
EASY
https://leetcode.com/problems/happy-number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


class Solution:

    MAX_TRIES = 1000  # get rid of this...

    def isHappy(self, n: int) -> bool:
        
        seen = set()  # if not happy, ends up in a loop

        def sum_of_squared_digits(n: int):
            s = 0
            while n != 0:
                n, digit = divmod(n, 10)
                s += digit ** 2
            return s

        for _ in range(self.MAX_TRIES):
            if n == 1:
                return True
            n = sum_of_squared_digits(n)
            if n in seen:
                return False
            else:
                seen.add(n)

        return False
