# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
         # stack
        stack = []  # [char, count (chars following each other)]
        
        for c in s:
            if len(stack) > 0 and stack[-1][0] == c:  # same character
                stack[-1][1] += 1
                
                if stack[-1][1] == k:
                    stack.pop()
                    
            else:  # first/different character
                stack.append([c, 1])
                
        return "".join(char * count for char, count in stack)       
        