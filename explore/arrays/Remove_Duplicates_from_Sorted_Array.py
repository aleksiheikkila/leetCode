# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        i = 1
        for j in range(1, len(nums)):
            if nums[i-1] != nums[j]:  # new value, keep
                nums[i] = nums[j]
                i += 1
            # else skip the value we already have
        
        return i  # new lenght
        