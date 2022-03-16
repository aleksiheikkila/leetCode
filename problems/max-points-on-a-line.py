""" 149. Max Points on a Line. HARD
https://leetcode.com/problems/max-points-on-a-line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.


#### Approach:
Consider each point in turn as a base point.

Then calculate the slope of the line formed by this point and every other point.
Consider the special case where we have the same point (slope undefined).
Max number of points that can be put on the same line with this base point is then:
    1 (this point) 
    + other points that are equal to "this point" (i.e. same point)
    + highest number of points having the same slope with this point

"""

# from decimal import Decimal  # for accurate calculations
from collections import Counter
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def slope(p1, p2) -> float:
            dx = p1[0] - p2[0]
            if dx == 0:
                return float("inf")
            dy = p1[1] - p2[1]
            return dy / dx
        

        N = len(points)
        max_pts = 0
        
        for i, p in enumerate(points):
            num_same_pts = 0
            slopes = []
            
            for j in range(N):
                if i == j: continue
                if p == points[j]:
                    num_same_pts += 1
                else:
                    slopes.append(slope(p, points[j]))
                            
            num_same_slope = Counter(slopes).most_common(1)
            num_same_slope = num_same_slope[0][1] if len(num_same_slope) == 1 else 0
            
            max_pts = max(max_pts, 1 + num_same_pts + num_same_slope)
        
        return max_pts
                