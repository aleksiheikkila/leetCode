""" 
1523. Count Odd Numbers in an Interval Range
Easy
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        nums = high - low + 1
        
        if nums % 2 == 0:
            return nums // 2
        else:
            return (nums // 2) if low % 2 == 0 else (nums // 2) + 1
