# https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2796/

# The way of transmitting the "found solution" signal thru the recursion stack is pretty clumsy

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # backtracking. Go row by row, col by col
        self.board = board
        
        if self.solveBoard(0, 0):
            #print("Found solution")
            return
        else:
            print("Could not find solution!")

        
    def solveBoard(self, row, col):
        """ Returns True if sol is found. Else False"""
        # base case: out of board, i.e. found solution
        # as each placed number has been valid
        if row >= 9:
            # found solution
            #print("FOUND SOLUTION!")
            return True
        
        # if contains a number, skip
        if self.board[row][col] != ".":
            # go to next pos that needs to be filled
            if self.solveBoard(*self.next_unsolved(row, col)):
                return True

        else:
            # check what are the valid numbers
            possible_nums = self.valid_nums_for_pos(row, col)
            for num in possible_nums:
                # place, and continue
                self.board[row][col] = str(num)
                
                if self.solveBoard(*self.next_unsolved(row, col)):
                    return True
                
                self.board[row][col] = "."
        
        return False
        

    def next_unsolved(self, row, col):
        """Gives index of the next unsolved from row, col. Or goes out of bounds"""
        while True:
            col = (col + 1) % 9
            if col == 0:
                row += 1
                if row >= 9:
                    return row, 0  # go there to signal "solution found"
            if self.board[row][col] == ".":
                return row, col
            

    def valid_nums_for_pos(self, row, col):
        nums = {str(i) for i in range(1, 10)}
        
        # row
        for el in self.board[row]:
            if el != ".":
                nums.discard(el)
        
        # col       
        for r in range(9):
            if r == row: continue
            if self.board[r][col] is not None:
                nums.discard(self.board[r][col])
             
        # subgrid
        subgrid_row = row // 3
        subgrid_col = col // 3
        
        for r in range(subgrid_row*3, subgrid_row*3 + 3):
            for c in range(subgrid_col*3, subgrid_col*3 + 3):
                 if self.board[r][c] != ".":
                    nums.discard(self.board[r][c])
        
        return nums
        