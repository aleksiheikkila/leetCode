# https://leetcode.com/problems/jump-game

# Slow

class Solution:

    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i, num in enumerate(nums):
            max_reach = max(max_reach, i+num)
            
            if i == max_reach:  # bump into barrier
                break
        
        return max_reach >= len(nums) - 1



    def canJump_old(self, nums: List[int]) -> bool:
        # slow
        # start from the end, mark for each index if one can finish from there
        
        if len(nums) == 1:
            return True
        
        last_idx = len(nums) - 1
        idx = last_idx - 1
        path_exists_from = {last_idx}
        min_step_required = 1
        
        while idx >= 0:
            num = nums[idx]
            if any(idx + a in path_exists_from for a in range(min_step_required, num + 1)):
                path_exists_from.add(idx)
                min_step_required = 1
            else:
                min_step_required += 1
            
            idx -= 1
        
        return True if 0 in path_exists_from else False
