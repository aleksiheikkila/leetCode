# https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicated = None
        missing = None
        seen = set()
        
        for n in nums:
            if n in seen:
                duplicated = n
            else:
                seen.add(n)
            
        # may need to go max(nums) + 1, if the largest value is the missing one
        for i in range(1, max(nums) + 2):
            if i not in seen:
                missing = i
                break
                
        return [duplicated, missing]
