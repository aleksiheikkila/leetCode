# https://leetcode.com/problems/next-permutation

# A bit awkward... could be made more clear/intuitive

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        # 1.
        # start from right, find first decreasing element
        # i.e. nums[i-1] < nums[i]
        i = len(nums) - 1
        while i >= 1:
            if nums[i-1] < nums[i]:
                #print(f"First decreasing from right at index {i-1}, val:{nums[i-1]}")
                break
            i -= 1
        
        if i == 0:
            # is fully descending, no next perm possible. Sort to asc order
            nums.sort()
            return
        else:
            # swap nums[i-1] to the next larger
            for j in range(i, len(nums)):
                if nums[j] <= nums[i-1]:
                    # then swap i-1 with j-1
                    #print(f"Number just larger at index {j-1}, val:{nums[j-1]}")
                    nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
                    break
            else:
                #print("Swapping with last num")
                nums[i-1], nums[-1] = nums[-1], nums[i-1]
                    
            # reverse right end to asc order
            left, right = i, len(nums) - 1
            
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            