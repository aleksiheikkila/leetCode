# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/

class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci with different starting conditions...
        # Kind of a dynamic programming approach
        ways_to_stair = {1: 1, 2: 2}
        
        for i in range(3, n + 1):
            # could be made faster without dict
            ways_to_stair[i] = ways_to_stair[i-1] + ways_to_stair[i-2]
            
        return ways_to_stair[n]
    