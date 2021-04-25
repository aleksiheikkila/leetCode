#https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valids = []
        
        def backtrack(stri, num_opening, num_closing):
            if len(stri) == 2 * n:
                valids.append(stri)
                return
            if num_opening < n:
                # can place opening parenthesis
                backtrack(stri + "(", num_opening + 1, num_closing)
            if num_closing < num_opening:
                # can place closing parenthesis
                backtrack(stri + ")", num_opening, num_closing + 1)
        
        backtrack("", num_opening=0, num_closing=0)
        
        return valids
    