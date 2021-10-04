# https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1, 1]]
        for rowno in range(2, numRows):
            prev_row = ans[rowno - 1]
            row = [1]
            for i in range(rowno - 1):
                row.append(prev_row[i] + prev_row[i+1])
            row.append(1)
            ans.append(row)
              
        return ans[:numRows]
