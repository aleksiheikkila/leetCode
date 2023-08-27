""" 
908. Smallest Range I
Easy
https://leetcode.com/problems/smallest-range-i/

You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to 
nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

"""
from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        """
        How to make score (max - min) smaller? Push min and max closer to each other.
        
        If min(nums) + k < max(nums) - k
        --> smallest score will be max(nums) - min(nums) - 2k
        
        else we can push every value to the same number and get score of 0
        """
        
        # could read min and max on one pass...
        
        return max(0, max(nums) - min(nums) - 2*k)
