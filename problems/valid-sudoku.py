# https://leetcode.com/problems/valid-sudoku

from collections import Counter

class Solution:
    
    def valid_bunch(self, counter):
        most_common = counter.most_common(1)
        return False if most_common and most_common[0][1] > 1 else True
        #    return False
        #else:
        #    return True
        
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.valid_bunch(Counter(el for el in row if el != ".")):
                return False
        
        for col in zip(*board):
            if not self.valid_bunch(Counter(el for el in col if el != ".")):
                return False
            
        for tile_row in range(3):
            tiles = [[], [], []]

            for rowno in range(tile_row * 3, tile_row * 3 + 3):
                for colno, val in enumerate(board[rowno]):
                    if val != ".":
                        tiles[colno // 3].append(val)
                        
            for tile in tiles:
                if not self.valid_bunch(Counter(tile)):
                    return False
                
        return True
