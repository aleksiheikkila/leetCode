# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # stack
        rst = []
        
        for c in s:
            # if the next char is the same as the one at the top of the stack
            if len(rst) > 0 and c == rst[-1]:  
                rst.pop()
            else:
                rst.append(c)
                
        return "".join(rst)
        