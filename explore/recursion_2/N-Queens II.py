# https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2804/

class Solution:
    def totalNQueens(self, n: int) -> int:
        # recursively, row by row
        # on each row, try to place the queen on each col
        # check if it is safe move or not
        # if it is, recurse to the next row
        # if we go past the last row, without hitting invalid pos, weve found a sol
        
        self.n = n
        self.queens = set()   # contains tuples (row, col)
        self.num_solutions = 0
        
        # start the recursion
        self.totalNQueens_helper(0)
        
        return self.num_solutions
        
        
    def totalNQueens_helper(self, row):
        # recursive
        
        # base case: we have went past the last row
        if row >= self.n:
            self.num_solutions += 1
            return
        
        
        for col in range(self.n):        
            if self.is_valid_move(row, col):
                self.place_queen(row, col)
                self.totalNQueens_helper(row + 1)
                self.remove_queen(row, col)  # for the next col
    
        return 
            
            
    def place_queen(self, row, col):
        self.queens.add((row, col))
        
    def remove_queen(self, row, col):
        # assumes the queen is there...
        self.queens.remove((row, col))
        
    def is_valid_move(self, row, col):
        for (queen_row, queen_col) in self.queens:
            if row == queen_row or col == queen_col:
                return False
            if abs(row - queen_row) == abs(col - queen_col):
                # diagonal
                return False
        return True
        
        