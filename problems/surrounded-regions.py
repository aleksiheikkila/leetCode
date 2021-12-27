# https://leetcode.com/problems/surrounded-regions
# Medium

# DFS, stack

from collections import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        NROWS, NCOLS = len(board), len(board[0])
        stack = []
        
        # find Os at the border. Then explore by dfs to adjacent cells
        
        # explore top and bottom borders
        for r in (0, NROWS-1):
            for c in range(NCOLS):
                if board[r][c] == "O":
                    stack.append((r,c))
        
        # explore left and right borders
        for c in (0, NCOLS-1):
            for r in range(1, NROWS-1):
                if board[r][c] == "O":
                    stack.append((r,c))
        
        keep_o = set(stack)  # the border Os are safe
        
        # DFS
        # Check conditions and add to keep_o at addition-time
        while stack:
            r, c = stack.pop()
            
            # add possible O adjs to stack and solution set
            for rr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if (0 <= rr < NROWS and 0 <= cc < NCOLS 
                and board[rr][cc] == "O" and (rr, cc) not in keep_o):
                    keep_o.add((rr, cc))
                    stack.append((rr, cc))
        
        # construct the board after captures
        for r in range(NROWS):
            for c in range(NCOLS):
                if (r,c) in keep_o:
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
        
        # no not return anything: changes made to board in place
