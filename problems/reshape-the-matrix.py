# https://leetcode.com/problems/reshape-the-matrix

class Solution:
    def matrixReshape2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c or r < 1 or c < 1:
            return mat
        
        reshaped = [[] for _ in range(r)]
        i = 0
        for row in mat:
            for n in row:
                reshaped[i // c].append(n)
                i += 1
                
        return reshaped
    
    
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:  # or r < 1 or c < 1:
            return mat

        #reshaped = []
        items = [n for row in mat for n in row]

        #for i in range(r):
        #    reshaped.append(items[i*c:(i+1)*c])
        #return reshaped
        
        return [items[i*c:(i+1)*c] for i in range(r)]
                