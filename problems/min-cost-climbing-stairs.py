# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        # rolling cost
        rc = cost[:2]

        for i in range(2, len(cost)):
            rc[0], rc[1] = rc[1], min(rc[:2]) + cost[i]

        return min(rc)
        