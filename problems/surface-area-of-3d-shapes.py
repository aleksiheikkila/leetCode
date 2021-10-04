# https://leetcode.com/problems/surface-area-of-3d-shapes

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 0
        
        grd = {}
        for rowno, row in enumerate(grid):
            for colno, val in enumerate(row):
                grd[(rowno, colno)] = val
        
        for r in range(nrows):
            for c in range(ncols):
                h = grd[(r, c)]
                area += 2 if h > 0 else 0
                for dr, dc in DELTAS:
                    area += max(0, h - grd.get((r+dr, c+dc), 0))
                          
        return area
