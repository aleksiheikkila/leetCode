# https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
 
        # Search the pivot point
        left, right = 0, len(nums) - 1
        right_part_start_idx = len(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[0]:
                # in right part
                right_part_start_idx = mid
                right = mid - 1
            else:
                # in left part
                left = mid + 1
                
        #print("Right part starts at index:", right_part_start_idx)
         
        # Then search the correct part
        if nums[0] == target:
            return 0
        elif nums[0] < target:
            # search before pivot, left part
            left, right = 0, right_part_start_idx - 1
        else:
            # search after pivot, right part
            left, right = right_part_start_idx, len(nums) - 1
        
        # do binary search
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # not found
        return -1
        