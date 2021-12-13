# https://leetcode.com/problems/random-pick-with-weight

import random
from bisect import bisect_left
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        # w ints are >= 1
        # cumulative w
        self.cum_w = []
        prev = 0
        for num in w:
            self.cum_w.append(prev + num)
            prev = self.cum_w[-1]
        # so all values in cum_w are >= 1
        # and the last one is the largest

        
    def pickIndex(self) -> int:
        # Using bisect... which one is the right one?
        # bisect_left: Locate the insertion point for x in a to maintain sorted order. 
        # If x is already present in a, the insertion point will be before (to the left of) 
        # any existing entries.
        return bisect_left(self.cum_w, random.randint(1, self.cum_w[-1]))
        # randint includes the ending value


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
