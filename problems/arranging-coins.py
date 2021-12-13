# https://leetcode.com/problems/arranging-coins
# Math solution

# 1 + 2 + .. + k <= n  (1)
# max k [int] satisfying this is the answer!

# Reduced formula for the sum series: sum(i), i=1...k = k*(k+1)/2
# Example: 1 + 2 + 3 + 4 + 5 = 15
# k*(k+1)/2 = (5*6)/2= 15. OK

# (1) becomes:
# k**2 + k <= 2n  (2)

# Observe: (k + 1/2)^2 = k^2 + 2*(1/2)*k + 1/4 = k^2 + k + 1/4
# Then (2): (k + 1/2)^2 - (1/4) = 2n
# Solve for k
# k = sqrt(2n + 0.25) - 1/2... then floor it

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt(2*n + 0.25) - 0.5)
        