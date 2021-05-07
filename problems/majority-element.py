# https://leetcode.com/problems/majority-element

# TODO: Make faster

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        majority_threshold = len(nums) // 2
        
        for num in nums:
            counts[num] += 1
            if counts[num] > majority_threshold:
                return num
            