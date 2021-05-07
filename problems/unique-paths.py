# https://leetcode.com/problems/unique-paths/

# Math solution also possible.
# its a permutations problem. How many ways is to have m-1 "DOWN steps" and n-1 "RIGHT steps".

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP, with less mem usage
        dp = [1] * n
        
        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c-1] + dp[c]
           
        return dp[-1]
    

    def uniquePaths_old(self, m: int, n: int) -> int:
        # DP, with unnecessarily large memory footprint
        uniq_paths_to = [[0 for _ in range(n) ] for _ in range(m)]
        uniq_paths_to[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                uniq_paths_to[r][c] = (uniq_paths_to[r][c-1] if c > 0 else 0) + \
                                    (uniq_paths_to[r-1][c] if r > 0 else 0)
                
        return uniq_paths_to[m-1][n-1]
