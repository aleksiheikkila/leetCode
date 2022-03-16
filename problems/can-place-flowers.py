# https://leetcode.com/problems/can-place-flowers

from math import ceil

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # shortcuts:
        if n <= 0:
            return True
        
        L = len(flowerbed)
        # too many plants:
        if n > ceil(L/2):
            return False
        
        # let's not modify the original list
        flowers = flowerbed.copy()
        
        # proceed in greedy way
        for i in range(L):
            # free spot: are adjacents free too?
            if (not flowers[i] 
                    and (i == 0 or flowers[i-1] == 0) 
                    and (i == L-1 or flowers[i+1] == 0)):
                if n == 1:
                    return True
                flowers[i] = 1
                n -= 1
        
        # Could not fit the plants        
        return False
        