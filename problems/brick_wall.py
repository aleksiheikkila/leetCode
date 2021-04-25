# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3717/

from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cracks = defaultdict(int)
        
        for row in wall:
            pos = -1
            for el in row[:-1]:
                pos += el
                cracks[pos] += 1
        
        if len(cracks.values()) > 0:
            return len(wall) - max(cracks.values()) 
        else:
            return len(wall)
        