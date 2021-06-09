# https://leetcode.com/problems/permutations

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])]


    def dfs(self, nums, cand, result):
        if len(nums) == 0:
            result.append(cand)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], cand + [nums[i]], result)


    def permute_dfs(self, nums: List[int]) -> List[List[int]]:
        """DFS-based"""
        result = []
        self.dfs(nums, [], result)

        return result



    """Slow"""
    
    def _perm(self, nums: list, used_idx: set, candidate: list):
        if len(candidate) == len(nums):
            self.result.append(candidate[:])
            return
        
        for i in range(len(nums)):
            if i in used_idx:
                continue
            candidate.append(nums[i])
            used_idx.add(i)
            self._perm(nums, used_idx, candidate)
            candidate.pop()
            used_idx.remove(i)
            
    
    def permute2(self, nums: List[int]) -> List[List[int]]:
        # permutation is an arrangement of the element to a sequence
        
        # [1] -> [1]
        # [1,2] -> [1,2], [2,1]
        # [1,2,3] -> [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
        
        # For the first slot, try each value, and recursively call for the remaining

        
        self.result = []
        used_idx = set()
        candidate = []
        
        self._perm(nums, used_idx, candidate)
        
        return self.result
    