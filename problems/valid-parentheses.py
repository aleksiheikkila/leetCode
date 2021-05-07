# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        # Using a stack

        OPENING = {"(", "[", "{"}
        #CLOSING = {")", "]", "}"}
        MATCHING_OPENING = {")": "(",
                            "]": "[",
                            "}": "{"}
        stack = []
        
        for c in s:
            if c in OPENING:
                stack.append(c)
            else:
                # consist of parentheses only, so these are then CLOSING ones
                if len(stack) == 0 or stack.pop() != MATCHING_OPENING[c]:
                    return False
                
     
        return len(stack) == 0
        