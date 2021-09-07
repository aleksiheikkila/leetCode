# https://leetcode.com/problems/01-matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # return the same matrix mat
        # DP, strategy

        # 1. scan from top to bottom (left to right)
        # set the shortest distance to a cell, based on the shortest distance 
        # to the above and the cell to the left (that have been processed already)
        #
        # 2. scan in the reverse direction
        # set the shortest dist based on what we already had from top and left
        # and what we now have available on right and bottom directions
        # take the minimum
        
        nrows, ncols = len(mat), len(mat[0])
        
        # 1. from top-left, row-wise to bottom-right
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val > 0:  # if val == 0, it's already correct
                    top = mat[i-1][j] if i > 0 else float("inf")
                    left = mat[i][j-1] if j > 0 else float("inf")
                    mat[i][j] = min(top, left) + 1
        
        # 2. scan in the reverse direction
        for i in reversed(range(nrows)):
            for j in reversed(range(ncols)):
                val = mat[i][j]
                if val > 0:
                    bottom = mat[i+1][j] if i < nrows - 1 else float("inf")
                    right = mat[i][j+1] if j < ncols - 1 else float("inf")
                    # now set the final shortest distances
                    # so its the min from either (top, left, bottom, right)
                    mat[i][j] = min(val, bottom + 1, right + 1)
        
        return mat
