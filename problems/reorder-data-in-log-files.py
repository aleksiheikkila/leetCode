# https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #rst = []
        rst = []
        digit_logs = []
        
        for line in logs:
            if line.split(" ")[1][0].isalpha():
                rst.append(line)
            else:
                digit_logs.append(line)
                
        rst.sort(key= lambda x: (x.split(" ")[1:], x.split(" ")[0]))           
        rst.extend(digit_logs)    
        
        return rst
