# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/

class Solution:
        
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        
        # find parent... its at the k-index: ceil(K/2) on the prev row
        parent = self.kthGrammar(N-1, K//2 + K%2)  # either 0 or 1
        odd_K = (K % 2 == 1)  # which position of the pair we are at... even or odd index
        
        if parent == 0:
            # generates pair 01
            return 0 if odd_K else 1  
        else:  
            # generates pair 10
            return 1 if odd_K else 0


 def kthGrammar_crappy(self, N: int, K: int) -> int:
     # Naive, super slow. Never use
    row = [0]
    rowno = 1
    
    while rowno < N:
        new_row = []
        for num in row:
            if num == 0:
                new_row.extend([0, 1])
            else:
                new_row.extend([1, 0])
            
        row = new_row    
        rowno += 1
        
    return row[K - 1]
    