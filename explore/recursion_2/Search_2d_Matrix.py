# https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2872/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0][0] == target:
            return True
        
        # midway col
        midcol = len(matrix[0]) // 2
        
        # find the row to divide
        pivot_row = len(matrix) - 1
        for rowno in range(len(matrix)):
            if matrix[rowno][midcol] == target: return True
            if matrix[rowno][midcol] > target:
                pivot_row = rowno
                break
                
        # search upper right
        upper_right_matrix = [[el for el in row[midcol+1:]] for row in matrix[:pivot_row+1]]
        #print("upper_right_matrix", upper_right_matrix )
        found_right = self.searchMatrix(upper_right_matrix, target)
        if found_right:
            return True
        # lower left
        lower_left_matrix = [[el for el in row[:midcol]] for row in matrix[pivot_row:]]
        #print("lower left:", lower_left_matrix)
        found_left = self.searchMatrix(lower_left_matrix, target)
        if found_left:
            return True
        
        return False