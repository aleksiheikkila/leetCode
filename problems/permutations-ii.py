# https://leetcode.com/problems/permutations-ii

class Solution:
    """Slow"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])]
    

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        
        for cand in self.permute(nums):
            if tuple(cand) in seen:
                continue
            seen.add(tuple(cand))
            result.append(cand)
            
        return result
