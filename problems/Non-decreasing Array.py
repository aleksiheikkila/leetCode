# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3731/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        
        violations = 0
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                # decreasing part, i.e. violation
                violations += 1
                if violations > 1:
                    return False
                # Need the determine which value, i or i-1, needs to be changed
                if i == 1 or nums[i-2] <= nums[i]:
                    # if we are at the start, or 
                    nums[i-1] = nums[i]

                else:  # nums[i-2] > nums[i]  --> need to lift nums[i] up
                    nums[i] = nums[i-1]
                
        return True
        