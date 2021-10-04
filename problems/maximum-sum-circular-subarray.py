# https://leetcode.com/problems/maximum-sum-circular-subarray

def kadane(nums) -> int:
    """Returns the maximum subarray sum"""
    max_ending_here = 0 
    max_so_far = float("-inf")
    
    for n in nums:
        max_ending_here += n
    
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # two possibilities:
        # 1) max subsequence doesn't wrap around --> find with kadane
        # 2) wraps around
        
        # Corner case: all values negative... return the maximum 
        m = max(nums)
        if m < 0:
            return m
        
        # Possibility 1:
        max_linear = kadane(nums)
        
        # Possibility 2
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            nums[i] = -nums[i]
            
        
        # with inverted array, kadane finds the part that is the minimum subarray sum in the ORIGINAL
        max_wraparound = total_sum + kadane(nums)
        # this kadane of inverted array gives the max (linear) subarray sum of inverted
        # -kadane is the minimum subaray sum, non-contributing part
        # total_sum - (-kadane) is the max subarray with wraparound
        
        return max(max_linear, max_wraparound)