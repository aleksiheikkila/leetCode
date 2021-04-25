# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # iterative binary search
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[mid+1]:
                # on an asc slope
                left = mid + 1
            else:  # this is the > case: subsequent values are never same
                # on a desc slope
                right = mid

        return left
        