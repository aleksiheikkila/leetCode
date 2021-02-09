# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 2:
            return nums
        
        # two-pointer approach
        writepointer = 0
        
        # get rid of the zeros, retain order
        for readpointer in range(len(nums)):
            if nums[readpointer] != 0:
                nums[writepointer] = nums[readpointer]
                writepointer += 1
                
        # fill the zeros
        for i in range(writepointer, len(nums)):
            nums[i] = 0
                