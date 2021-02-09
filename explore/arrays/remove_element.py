# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two-pointer technique
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            # else skip the to-be-removed value
                
        return i  # new length (used as a new len downstream)
        