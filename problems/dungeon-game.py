# https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        NROWS, NCOLS = len(dungeon), len(dungeon[0])
        
        # DP
        # minimum hp to enter a specific room
        # add one extra row and col. Init with large values
        min_hp = [[float("inf") for _ in range(NCOLS + 1)] for _ in range(NROWS + 1)]
        # Memory usage could be optimized: no need to keep track of all of it!
        
        # min_hp[NROWS-1][NCOLS-1] = max(1, 1 - dungeon[-1][-1])  
        
        for r in range(NROWS-1, -1, -1):
            for c in range(NCOLS-1, -1, -1):
                # last room:
                if c == NCOLS - 1 and r == NROWS - 1:
                    min_hp[r][c] = max(1, 1 - dungeon[r][c])
                # other rooms: consider whether to go to DOWN or RIGHT
                else:
                    min_hp[r][c] = max(1, min(min_hp[r+1][c], min_hp[r][c+1]) - dungeon[r][c])
                    
        return min_hp[0][0]
    