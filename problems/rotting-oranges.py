# https://leetcode.com/problems/rotting-oranges
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        DIRECTIONS = ((-1, 0), (0, -1), (1, 0), (0, 1))
        nrows, ncols = len(grid), len(grid[0])
        
        count_fresh = time = 0
        rotten = []  # stack

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                
                if val == 2:
                    rotten.append((i, j))
                elif val == 1:
                    count_fresh += 1
        
        # no fresh oranges to begin with
        if count_fresh == 0:
            return 0
        
        # rotten contains only the new rotten oranges
        while rotten:
            time += 1
            new_rotten = [] # put here the new rotten oranges, then assign this to rotten
            while rotten:
                rotten_loc = rotten.pop()
                for di, dj in DIRECTIONS:
                    i = rotten_loc[0] + di
                    j = rotten_loc[1] + dj
                    
                    if 0 <= i < nrows and 0 <= j < ncols and grid[i][j] == 1:
                        # fresh orange becomes rotten
                        count_fresh -= 1
                        if count_fresh <= 0:
                            return time
                        
                        grid[i][j] = 2  # make it rotten
                        new_rotten.append((i, j))  # then process these in the next step
                
            rotten = new_rotten
          
        # if we reach this, there are oranges left that wont get rotten
        return -1
  