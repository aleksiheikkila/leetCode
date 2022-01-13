# https://leetcode.com/problems/maximal-rectangle/submissions/
# HARD

"""
Making use of the solution for https://leetcode.com/problems/largest-rectangle-in-histogram/

Approach:

Consider increasing number of rows separately. First the top row, then top 2 rows, ..., all rows
Construct a histogram
Apply the function from the leetcode prob 84 to find the largers area in that histogram

"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        NROWS = len(matrix)
        #NCOLS = len(matrix[0])
        
        max_area = 0
        
        def convert_to_histogram(rows):
            NCOLS = len(rows[0])
            histogram = [0] * NCOLS
            
            # could go in reverse order... 
            # so when zero is encountered, no need to check what is above it
            for row in rows:
                for col_idx in range(NCOLS):
                    if row[col_idx] == "0":
                        histogram[col_idx] = 0
                    else:
                        histogram[col_idx] += 1
                        
            return histogram
                        
                        
        def largestRectangleArea(heights: List[int]) -> int:
            """ More comments in the solution for leetcode problem 84"""
            max_area = 0
            s = []  # stack of indices

            for i, h in enumerate(heights + [0]): 
                while s and heights[s[-1]] > h:
                    block_h = heights[s.pop()]

                    # determine width
                    if not s: 
                        block_w = i
                    else: 
                        block_w = i - s[-1] - 1
                    max_area = max(max_area, block_h * block_w)
   
                s.append(i)

            return max_area

        
        for i in range(NROWS):
            hist = convert_to_histogram(matrix[:i+1])
            max_area = max(max_area, largestRectangleArea(hist))
            
        return max_area
        