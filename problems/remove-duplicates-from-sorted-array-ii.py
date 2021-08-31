# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

# Max 2 elements with the same value.
# Array in non-decreasing order

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # non-decreasing... the duplicates are back to back
        if len(nums) < 3:
            return len(nums)
        
        write_idx = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[write_idx-2] == nums[write_idx-1]:
                continue
            else:
                nums[write_idx] = nums[i]
                write_idx += 1
                
        return write_idx  
        