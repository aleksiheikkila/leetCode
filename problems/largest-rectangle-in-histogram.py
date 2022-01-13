# https://leetcode.com/problems/largest-rectangle-in-histogram/
# HARD

# Sliding window


"""
Naive approach could be to consider every subarray, calculate min height for that 
and then do height * width. O(N^2).


** Increasing stack based approach: ** 
Keep a (increasing height) stack of bars (heights, positions/indices) 
so that the top of stack is the highest bar in the stack.

Loop thru bars.
When we see a bar that:
- is lower than the previous one in the stack, pop those from stack and determine their areas
- is higher than the previous ones in the stack (or stack empty), add to stack

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        s = []  # stack of indices for non-decreasing bars
        
        for i, h in enumerate(heights + [0]):  
            # add zero to force calculations in the end (n), 
            # so that every valid area would get popped

            # Pop those from stack that are larger than the current
            # "cannot be extended to right".
            # Process their areas. What is the width?
            # if we don't have anything in the stack after popping,
            # its from the beginning (so width = i, from 0 to i-1).
            # Else it is from s[-1]+1 to i-1 
            # => i-1-(s[-1]+1)+1 = i - s[i] - 1
            while s and heights[s[-1]] > h:
                block_h = heights[s.pop()]
                # determine width:
                if not s: 
                    block_w = i
                else: 
                    block_w = i - s[-1] - 1
                max_area = max(max_area, block_h * block_w)
                #print(i, h, block_h, block_w, block_h * block_w, max_area)
            
            # add to stack (need to add also the case where h==heights[s[-1]])
            s.append(i)
                
        return max_area
        
    
    
    def largestRectangleArea_slow(self, heights: List[int]) -> int:
        # TOO SLOW
        from collections import defaultdict

        max_area = 0
        h_to_w = defaultdict(int)
        
        heights.append(-1)  # to check the last row
        
        prev = 1
        
        for pos, h in enumerate(heights):               
            if h > prev or pos == 0:
                # increasing, need to add
                for level in range(1, h+1):
                    h_to_w[level] += 1     
                    #if h_to_w[level] * level > max_area:
                    #        max_area = h_to_w[level] * level
                
            else:
                # decreased
                # need to rem
                for level in list(h_to_w):
                    if level > h:
                        # check until the prev. if it was max
                        if h_to_w[level] * level > max_area:
                            max_area = h_to_w[level] * level
                        h_to_w[level] = 0
                    else:
                        h_to_w[level] += 1
                        #if h_to_w[level] * level > max_area:
                        #    max_area = h_to_w[level] * level
                            
                            
            prev = h
            #print(max_area)

        return max_area