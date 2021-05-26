# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """2 * sum(set(nums)) - sum(nums) is the value that occured only once"""
        return 2*sum(set(nums)) - sum(nums) 
        