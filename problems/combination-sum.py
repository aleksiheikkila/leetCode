# https://leetcode.com/problems/combination-sum

class Solution:
    def _backtrack(self, target, start_idx, curr_comb):
        # Base case A (this is not actually called)
        if target < 0:
            return  # invalid combination, return and backtrack
        # Base case B:
        if target == 0:
            self.result.append(curr_comb[:])  # need to copy to result
            return
        for i in range(start_idx, len(self.cands)):
            # this start_idx takes care of the duplication
            cand = self.cands[i]
            if cand > target:
                return  # invalid... the candidates list is sorted, so we can stop
            curr_comb.append(cand)
            self._backtrack(target - self.cands[i], i, curr_comb)
            curr_comb.pop() 
            
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cands = sorted([c for c in candidates if c <= target])
        self.result = []
        self._backtrack(target, 0, [])

        return self.result
        