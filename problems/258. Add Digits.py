""" 258. Add Digits
Easy

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            s = 0
            while num > 0:
                num, digit = divmod(num, 10)
                s += digit
            num = s
                
        return num
