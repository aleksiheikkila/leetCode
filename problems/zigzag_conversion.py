# https://leetcode.com/problems/zigzag-conversion/submissions/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        r, dr = 0, -1

        for c in s:
            rows[r].append(c)
            if r == 0 or r == numRows - 1:
                dr *= -1
            r += dr


        rst = []
        return "".join(rst.expand(row) for row in rows)
            