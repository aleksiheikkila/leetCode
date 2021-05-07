# https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Can move only down or right makes it easier
        nrows, ncols = len(grid), len(grid[0])
        
        # cumsums for the first row
        dp = [grid[0][0]]
        for c in range(1, ncols):
            dp.append(dp[-1] + grid[0][c])
            
        # then go thru, each dp is the current cell value + min "from_left" "from_up"
        for r in range(1, nrows):
            for c in range(ncols):
                dp[c] = grid[r][c] + min(dp[c-1] if c>0 else float("inf"), dp[c])
                
        return dp[-1]
                