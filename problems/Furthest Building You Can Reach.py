#import bisect
from queue import PriorityQueue

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Use first all bricks
        # put jumps to priorityqueue giving out the max jumps     
        q = PriorityQueue()  # holds all jumps covered by bricks.
        # get gives lowest value, so jumps are stored in as -jump
        prev_h = heights[0]
        
        for i, h in enumerate(heights):
            if h <= prev_h:
                prev_h = h
                continue
                
            jump = h - prev_h
            
            if jump <= bricks:
                # use bricks first
                q.put(-jump)
                bricks -= jump
                
            elif ladders > 0:
                # not enough bricks, then use ladders if possible
                ladders -= 1
                # Check if its better to use them earlier
                if not q.empty():
                    max_gap = q.get()  # most negative this far
                    if -max_gap > jump:
                        # use earlier
                        q.put(-jump)  # use bricks here
                        bricks = bricks - max_gap - jump  # max_gap is negative, hence the minus...
                    else:
                        q.put(max_gap)  # do not swap, put back
  
            else: # no bricks or ladders left
                return i - 1
            
            prev_h = h
        
        return i
    