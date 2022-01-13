# https://leetcode.com/problems/longest-valid-parentheses
# HARD

# Stack

"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

#####
Keep a stack with indices
Keep at the first value (leftmost) the last index before valid segment starts. Init to -1.


Example input: ")()())"
=>
init s = [-1] 
step 1: ) -> pop, then because is empty add index to stack: s = [0]
step 2: ( -> append index: s = [0, 1]
step 3: ) -> pop, calculate lenght: s = [0] & len 2 - 0 = 2
step 4: ( -> append index: s = [0, 3]
step 5: ) -> pop, calculate length: s = [0] & len 4-0 = 4 (new max len)
step 6: ) -> pop, then because is empty add index: [5] 
(this would be the new "one before valid segment")

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # initialize stack
        
        for idx, c in enumerate(s):
            if c == "(":
                stack.append(idx)
            else: # closing parenthesis
                stack.pop()  # we will always have a value here, thanks to the init
                if not stack:
                    # we came to invalid segment. Add this index to be the new 
                    # "one before the valid segment"
                    stack.append(idx)
                else:
                    # ok, popped out a matching opening parentheses, check the length
                    max_len = max(max_len, idx - stack[-1])
        
        return max_len
      