# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted

from typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Three possible cases
        # 1. Remove left side
        # 2. Remove right side
        # 3. Remove something from the middle
        
        min_len = 0
        N = len(arr)
        
        left, right = None, N - 1
        for i in range(1, N):
            if arr[i] < arr[i - 1]:
                # violation, decreasing
                left = i - 1  # last valid index from left
                # Case 2: would need to remove arr[left+1:]
                break  
                
        if left is None:
            # was already sorted, no need to remove anything
            return 0
                
        for i in reversed(range(N - 1)):
            if arr[i] > arr[i + 1]:
                # violation, decreasing
                right = i + 1  # last valid index from right
                # Case 1: would need to remove arr[:right]
                break
        
        min_len = min(right, N - left - 1)
                
        # Removing something from the middle?
        # for each num in sorted left, find first elem in sorted right that is larger than it
        # Removing those in between results in sorted array
        # Search for the smallest such subarray
        for left_idx in range(left + 1):
            for right_idx in range(right, N):
                if arr[left_idx] <= arr[right_idx]:
                    # remove between these indices, excl.
                    min_len = min(min_len, right_idx - left_idx - 1)
                    break
                    
        return min_len      
