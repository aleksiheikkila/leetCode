"""
179. Largest Number
Medium
https://leetcode.com/problems/largest-number/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
"""

from functools import cmp_to_key  
# Python3 does not have cmp. cmp_to_key can be used to turn a cmp-like function into key= param)

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        To the left we must get large digits.
        9 before 8 and so on.
        
        Longer than single digit nums should be compared alphabetically 
        when they are of similar length. Otherwise shorter is "bigger"?
        
        99 > 911.
        
        NO, DOES NOT work with e.g. [3, 34, 33]
        --> we should take 34 first.
        
        Correct way to compare:
        is x+y > y+x?  (referring to string concatenation)
        
        so lets compare 3 and 34:
        334 > 343? No, have 34 first
        
        33 and 34:
        3334 > 3433? No, take 34 first
        """
        
        def comp_func(num1: int, num2: int):
            if num1 == num2:
                return 0
            
            num1, num2 = str(num1), str(num2)
            
            if num1 + num2 > num2 + num1:
                return 1
            else:
                return -1

        # int in the middle to get rid of "00" kind of result (collapse to single zero digit)
        return str(int("".join(map(str, sorted(nums, 
                                               key=cmp_to_key(comp_func), 
                                               reverse=True)))))
