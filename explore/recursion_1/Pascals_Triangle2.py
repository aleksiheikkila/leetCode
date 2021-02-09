# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/

class Solution:
    def getRow_iter(self, rowIndex: int) -> List[int]:
        # iterative
        row = [1]
        
        for idx in range(1, rowIndex + 1):
            new_row = [0] * (idx + 1)
            for i, el in enumerate(new_row):
                if i == 0 or i == idx:
                    new_row[i] = 1
                else:
                    new_row[i] = row[i-1] + row[i]
            
            row = new_row
                
        return row
    
    
    def getRow(self, rowIndex: int) -> List[int]:
        # quite fast
        def next_row(prev_row):
            row = [0] * (len(prev_row) + 1)
            row[0], row[-1] = 1, 1
            for i in range(1, len(row) - 1):
                row[i] = prev_row[i-1] + prev_row[i]  
            return row
                
        row = [1]
        for _ in range(rowIndex):
            # kind of recursive
            row = next_row(row)  # kind of iterator
        
        return row
        