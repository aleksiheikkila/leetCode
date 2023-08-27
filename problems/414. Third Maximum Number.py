""" 414. Third Maximum Number. Easy
https://leetcode.com/problems/third-maximum-number/

Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        if len(s) < 3:
            return s[-1]
        else:
            return s[-3]
            