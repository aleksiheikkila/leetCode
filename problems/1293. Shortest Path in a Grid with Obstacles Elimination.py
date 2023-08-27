""" 1293. Shortest Path in a Grid with Obstacles Elimination
HARD

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) 
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

#########

BFS problem with "3D" state

"""

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # BFS
        
        ROWS, COLS = len(grid), len(grid[0])
        target = (ROWS - 1, COLS - 1)
        
        queue = deque()  # contains (row, col, remaining_k)
        queue.append((0, 0, k))
        
        dist = {(0, 0, k): 0}  # keep track of distances
        
        DIRECTIONS = ((-1, 0), (1, 0), (0, 1), (0, -1))
        
        while queue:
            x, y, k = queue.popleft()
            
            if (x, y) == target:
                return dist[(x, y, k)]
                
            for dx, dy in DIRECTIONS:
                cand_x, cand_y = x + dx, y + dy
                
                # out of bounds
                if not (0 <= cand_x < ROWS and 0 <= cand_y < COLS):
                    continue
                    
                # decrement remaining k if the new position is blocked
                new_state = (cand_x, cand_y, k - grid[cand_x][cand_y])
                
                # already visited (with smaller or eq. distance) or violation
                if new_state in dist or new_state[2] < 0:
                    continue

                # add new position to queue
                queue.append(new_state)
                dist[new_state] = dist[(x, y, k)] + 1
                         
        # no solution
        return -1
