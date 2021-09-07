# https://leetcode.com/problems/search-a-2d-matrix

from typing import List
class Solution:
    
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for the prospective row
        nrows, ncols = len(matrix), len(matrix[0])
        
        left, right = 0, nrows-1
        rowno_of_interest = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1
                rowno_of_interest = mid
            else:
                return True

        row, left, right = matrix[rowno_of_interest], 1, ncols - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
            
        return False
        