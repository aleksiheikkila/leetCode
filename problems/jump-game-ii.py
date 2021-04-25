# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        """Gives min number of jumps. It is guaranteed there is solution(s)"""
        if len(nums) == 1:
            return 0
        
        last_idx = len(nums) - 1
        idx = last_idx - 1
        min_jumps_from_idx = [float("inf") for _ in range(len(nums)-1)] + [0]
        
        while idx >= 0:
            num = nums[idx]
            if num > 0:
                min_jumps_from_idx[idx] = min(1 + min_jumps_from_idx[idx + j]
                                        for j in range(1, min(num+1, last_idx - idx + 1)))

            idx -= 1
        
        return min_jumps_from_idx[0]
