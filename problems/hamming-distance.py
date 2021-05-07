# https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x > 0 or y > 0:
            x, modx = divmod(x, 2)
            y, mody = divmod(y, 2)
            if modx != mody:
                dist += 1
        
        return dist