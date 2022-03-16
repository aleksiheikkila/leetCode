""" 218. The Skyline Problem. HARD
https://leetcode.com/problems/the-skyline-problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city 
when viewed from a distance. Given the locations and heights of all the buildings, 
return the skyline formed by these buildings collectively.


###############
Approach:

create events: building starts, building ends.
Sort these by x so that we can process them in correct order


Keep track of "active buildings". Reqquirements:
- can add and remove buildings.
- can check the current max

It suffices to keep track of the active _heights_.
It does not matter to this problem if we have multiple buildings with the same height active 
and we kind of remove the wrong one...

So we would need kind of a sorted list. Lets use one from sortedcontainers.
    - add() is O(logN)
    - remove() is O(logN)
    - max value is at the end, so it's just a O(1) lookup
    
"""

from sortedcontainers import SortedList  # is this okay?
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []
        
        # 1. Get the events
        events = []  
        # Event structure: (x, h, type [0 is left, 1 is right])
        # for left events, put h in as -h
        # and sort so that for the same x, the highest left (new blgn) will be processed first!
        for b in buildings:
            events.append((b[0], -b[2], 0))
            events.append((b[1], b[2], 1))
            
        events.sort(key=lambda x: (x[0], x[1]))
        
        # 2. Process events and update heights, skyline
        heights = SortedList([0])  # heights is kept sorted
        # add zero for base comparison (to more easily handle edge cases)
        
        for event in events:
            # left, add new building (inverse h)
            if event[2] == 0:
                heights.add(-event[1])
               
            # right, remove building (remove any with that height...)
            else:
                heights.remove(event[1])  # removes by value
            
            
            # update skyline if there is a change in max height
            if not skyline or skyline[-1][1] != heights[-1]:
                skyline.append([event[0], heights[-1]])
        
        return skyline
    