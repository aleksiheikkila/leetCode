# https://leetcode.com/problems/k-closest-points-to-origin
# Medium

# Bisect, keep track of nearest points

from collections import List
import bisect
# bisect compares tuple elements elem by elem... as does sort

# TODO: Quicksort / Randomized QuickSelect


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """One liner.
        Could do better e.g. with Quicksort / Randomized QuickSelect"""
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
        
        
    def kClosest_slow_bisect(self, points: List[List[int]], k: int) -> List[List[int]]:
        """This is slow"""
        # first add first k to the tracker
        # first element is the squared distance, second is the point as a list
        nearest_k = [(p[0]**2 + p[1]**2, p) 
                        for p in points[:k]]
        
        nearest_k.sort()

        for p in points[k:]:
            dist_squared = p[0]**2 + p[1]**2
            if dist_squared < nearest_k[-1][0]:
                # need to add:
                nearest_k.pop()
                bisect.insort_left(nearest_k, (dist_squared, p))
            
        return [point for _, point in nearest_k]
            