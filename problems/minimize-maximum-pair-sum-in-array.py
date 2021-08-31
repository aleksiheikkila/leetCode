# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        # how to minimize maximum pair sum
        # assing nums to pairs so that the smallest is paired with the largest, etc.
        
        # assume we can mess around with the list (side effects ok)
        nums.sort()
        
        max_pair_sum = float("-inf")
        last_idx = len(nums) - 1
        
        for i in range(len(nums) // 2):
            max_pair_sum = max(max_pair_sum, nums[i] + nums[last_idx - i])
 
        return max_pair_sum
        
        # [3,5,2,3]
        # sorted [2,3,3,5]
        # pairs (2, 5), (3, 3)
        # max of these is 7
        
        # [3,5,4,2,4,6]
        # sorted [2, 3, 4, 4, 5, 6]
        # pairs (2,6), (3,5), (4,4), max 8
        
       
        
        