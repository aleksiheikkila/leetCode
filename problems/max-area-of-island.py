class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # scan to find land that has not been considered yet
        # considered = set(), put land coordinates that have been assigned
        # start island area counter
        
        # when island is completed, check is it's the new maximum
        R, C = len(grid), len(grid[0])
        
        max_area = 0
        
        # then repeat
        
        used = set()
        for rowno, row in enumerate(grid):
            for colno, v in enumerate(row):
                if v == 1 and (rowno, colno) not in used:
                    island_area = 0
                    s = [(rowno, colno)]
                    used.add((rowno, colno))
                    
                    while s:
                        r, c = s.pop()
                        island_area += 1
                        
                        if r > 0 and grid[r-1][c] == 1 and (r-1, c) not in used: 
                            s.append((r-1, c))
                            used.add((r-1, c))
                        if c > 0 and grid[r][c-1] == 1 and (r, c-1) not in used: 
                            s.append((r, c-1))
                            used.add((r, c-1))
                        if r < R-1 and grid[r+1][c] and (r+1, c) not in used: 
                            s.append((r+1, c))
                            used.add((r+1, c))
                        if c < C-1 and grid[r][c+1] == 1 and (r, c+1) not in used: 
                            s.append((r, c+1))
                            used.add((r, c+1))
                            
                    max_area = max(max_area, island_area)
                    
        return max_area
                    
                    
                