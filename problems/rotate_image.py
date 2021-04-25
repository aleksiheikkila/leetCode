# https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Transpose and reverse rows
        """
        
        # The required transformation can be done by first transposing and 
        # then reversing row element order.
        # (Not the most efficient though)
        
        # transpose
        # pos (row, col) is put to (col , row)
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # reverse rows
        for r in range(n):
            for i in range(n//2):
                matrix[r][i], matrix[r][n-i-1] = matrix[r][n-i-1], matrix[r][i]
                
        return matrix
        
# Alternative would be to directly swap the four values...
# Would be more efficient... but the indexes a bit tricky to code