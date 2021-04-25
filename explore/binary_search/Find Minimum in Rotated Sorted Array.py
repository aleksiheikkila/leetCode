# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/949/

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

class Solution:
    def findMin(self, nums: List[int]) -> int:       
        lo = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < lo:
                lo = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
                
        return lo
        