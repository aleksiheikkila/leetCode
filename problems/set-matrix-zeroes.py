# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        
        erase_rows, erase_cols = set(), set()  # rows and cols to be zeroed
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    erase_rows.add(r)
                    erase_cols.add(c)
        
        # do the zeroing:
        for r in erase_rows:
            matrix[r] = [0] * cols
        for c in erase_cols:
            for row in matrix:
                row[c] = 0
