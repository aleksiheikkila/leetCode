# https://leetcode.com/problems/h-index-ii
# Medium

# Binary search

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # O(log(n)), so binary search
        
        # if most influential is zero, h will be zero
        if not citations or citations[-1] == 0:
            return 0
        
        N = len(citations)
        left, right = 0, N-1
        
        while left < right:
            mid = (left + right) // 2
            
            # check for the violation.
            # there are N - mid papers from mid onward (including mid)
            if N - mid > citations[mid]:
                left = mid + 1
            else:
                right = mid  # right answer could be at mid, so we cant go to mid - 1
                
        return N - left
        