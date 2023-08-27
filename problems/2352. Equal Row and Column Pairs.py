""" 
https://leetcode.com/problems/equal-row-and-column-pairs/
MEDIUM

Given a 0-indexed n x n integer matrix grid, return the number of pairs (Ri, Cj) such that row Ri and column Cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e. an equal array).

"""

from typing import List
from collections import Counter

class Solution:
    def equalPairs_long(self, grid: List[List[int]]) -> int:
        rst = 0
        
        NROWS, NCOLS = len(grid), len(grid[0])
        counts = Counter()
        for row in grid:
            counts[tuple(row)] += 1
            
        for c in range(NCOLS):
            column = []
            for r in range(NROWS):
                column.append(grid[r][c])
                
            rst += counts[tuple(column)]
            
        return rst


    def equalPairs(self, grid: List[List[int]]) -> int:
        counts = Counter(zip(*grid))
        return sum(counts[tuple(row)] for row in grid)
