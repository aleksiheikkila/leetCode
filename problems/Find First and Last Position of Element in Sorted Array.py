# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3725/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        # binary search
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # then expand both ways to find the range
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # expand from mid  (could also be binary search...)
        if nums[mid] != target:
            return [-1, -1]
        
        left = mid
        while left >= 0:
            if nums[left] != target:
                break
            left -= 1
                        
        right = mid
        while right < len(nums):
            if nums[right] != target:
                break
            right += 1
            
        return [left+1, right-1]
        