# https://leetcode.com/problems/unique-binary-search-trees
# Medium

# BST
# Recursion
# Memoization / DP

from functools import lru_cache

class Solution:
    
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        # recursive
        # try having each n as the root, find out how many configurations there are on left and right
        # total nbr is the product of left and right configs (these are independent)
        # base case is left/right with zero or one node --> numTrees there is "1"
        
        # this greatly benefits from memoization as we keep on solving the same subprobs
        # -> lru_cache with unlimited mem
        
        # base case
        if n <= 1:
            return 1
        
        num_trees = 0
        
        for root in range(1, n+1):
            # split to left and right, and call recursively
            left = self.numTrees(root - 1)
            right = self.numTrees(n - root)
            
            num_trees += left * right
        
        return num_trees
    