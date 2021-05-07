# https://leetcode.com/problems/spiral-matrix

# too complex/hacky

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nrows, ncols = len(matrix), len(matrix[0])
        
        dr, dc = 0, 1
        r, c = 0, -1
        rst = []
        
        next_dir = {(0, 1): (1, 0),
                    (1, 0): (0, -1),
                    (0, -1): (-1, 0),
                    (-1, 0): (0, 1)}
        
        lap = 0
        for i in range(nrows*ncols):
            # time to switch direction?
            if (c == ncols - 1 - lap and r == lap) \
              or (c == ncols - 1 - lap and r == nrows - 1 - lap) \
              or (c == lap and r == nrows - 1 - lap and (dr,dc) == (0,-1)) \
              or (c == lap and r == lap + 1 and (dr,dc) == (-1,0)):
                if (dr, dc) == (-1, 0):
                    lap += 1
                dr, dc = next_dir[(dr, dc)]
                
            r += dr
            c += dc
            rst.append(matrix[r][c])
            
        return rst
         