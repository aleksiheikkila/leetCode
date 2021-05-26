# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Similar to single-number-ii:
        return (3*sum(set(nums)) - sum(nums)) // 2
        