# https://leetcode.com/problems/image-smoother

from itertools import product

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        NROWS, NCOLS = len(img), len(img[0])
        smoothed = [[0] * NCOLS for _ in range(NROWS)]
        
        DELTAS = list(product([-1, 0, 1], repeat=2))
        # need to turn into a list:
        # product gives an iterator, which will be exhausted. Leading to div by zero
        
        for rowno in range(NROWS):
            for colno in range(NCOLS):
                n = sum_ = 0
                
                for dr, dc in DELTAS:
                    if 0 <= rowno + dr < NROWS and 0 <= colno + dc < NCOLS:
                        n += 1
                        sum_ += img[rowno + dr][colno + dc]
                
                smoothed[rowno][colno] = sum_ // n
      
        return smoothed
        