# https://leetcode.com/problems/rotate-array

class Solution:
    def rotate_naive(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())
            
            
    def rotate(self, nums: List[int], k: int) -> None:
        if k is None or k <= 0:
            return  # not allowed
        
        # avoid doing multiple rounds
        k, end = k % len(nums), len(nums) - 1
        if k == 0:
            return
        
        # step 1: reverse first n - k elements
        self.reverse(nums, 0, end - k)
        
        # step 2: reverse rest
        self.reverse(nums, end - k + 1, end)
        
        # step 3: reverse whole array
        nums.reverse()
        #self.reverse(nums, 0, end)
        
        
    def reverse(self, nums, start, end):
        """Reverses values in nums array, from start to end indices, both ends included"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
