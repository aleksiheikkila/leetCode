# https://leetcode.com/problems/word-search


class Solution:
    """ Not very efficient. Backtrack """
    def get_adj_pos(self, row, col):
            adjs = []
            if row > 0:
                adjs.append((row-1, col))
            if row < self.nrows - 1:
                adjs.append((row+1, col))
            if col > 0:
                adjs.append((row, col-1))
            if col < self.ncols - 1:
                adjs.append((row, col+1))
            
            return adjs
        
        
    def step(self, row, col, chars_left):
            # Found the word from the board!
            if len(chars_left) == 0:
                return True
            
            self.used.add((row, col))
            next_char = chars_left[0]
            
            possible_next_pos = [(r,c) for (r,c) in self.get_adj_pos(row,col) 
                    if ((r,c) not in self.used and self.board[r][c] == next_char)]
            
            for (r,c) in possible_next_pos:
                rst = self.step(r, c, chars_left[1:])
                if rst:
                    return True
                 
            self.used.remove((row, col))
            return False
    
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.nrows, self.ncols = len(board), len(board[0])
        self.board = board
        #self.word = word
        
        self.used = set()
        
        # find starting candidates.
        starting_pos = [(r,c) 
                        for r in range(self.nrows)
                        for c in range(self.ncols)
                        if self.board[r][c] == word[0]]

        for (r,c) in starting_pos:
            rst = self.step(r, c, word[1:])
            if rst:
                return True
            
        return False
        # the from each, try to go deeper.
        # for every step, check what adjacent cells have the required next char
        
        # backtrack
        