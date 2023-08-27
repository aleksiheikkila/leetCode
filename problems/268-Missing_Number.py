""" 268. Missing Number
Easy

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
from typing import List

class Solution:
    def missingNumber_1(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num != i:
                return i
        return len(nums)
    
    def missingNumber_series(self, nums: List[int]) -> int:
        """ Sum from 0 to N is: N * (N+1) / 2.

        Substract the actual sum in the nums list.
        
        
        """
        n = len(nums)
        return int((n * (n+1) / 2) - sum(nums))

    
