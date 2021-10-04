# https://leetcode.com/problems/where-will-the-ball-fall

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        RIGHT, LEFT = 1, -1
        
        # in a cell which slopes to right (ball going to right)
        # if next cell (one to right slopes to right, can go)
        # else blocked
        
        # blocked also is pushed to a wall
        answer = []
        
        NROWS, NCOLS = len(grid), len(grid[0])
        
        # Build grid
        g = {}
        for rowno, row in enumerate(grid):
            for colno, val in enumerate(row):
                g[(rowno, colno)] =  val
              
        # Drop a ball from each column
        for start_col in range(NCOLS):
            r, c = 0, start_col
            
            while r < NROWS:
                if g[(r,c)] == RIGHT:
                    if g.get((r, c + 1), LEFT) == LEFT:
                        # blocked
                        c = -1
                        break
                    c += 1
                        
                elif g[(r,c)] == LEFT:
                    if g.get((r, c - 1), RIGHT) == RIGHT:
                        # blocked
                        c = -1
                        break
                    c -= 1
                        
                r += 1
                
            answer.append(c)
            
        return answer