# https://leetcode.com/problems/regular-expression-matching

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        """top-down approach with cache/memoization"""
        
        cache = {}  # key (i, j), val isMatch bool
        
        def dfs(i:int, j:int) -> bool:
            # i refers to index in s
            # j to index in p
            if (i,j) in cache:
                return cache[(i,j)]
            
            # base cases
            if i >= len(s) and j >= len(p):
                # matches
                return True
            if j >= len(p):
                # pattern exhausted, still string left
                return False
            
            # if i >= len(s) but j < len(p) --> to be seen, can go either way

            # check if the strings char and pattern match
            # handle the case i is out of bounds
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # check if we are at starred pattern character
            if (j+1) < len(p) and p[j+1] == "*":
                # two possibilities:
                # 1) can skip the * char... then incr j by two (hop over the *)
                # 2) can use the * char IF those match... then incr i by one
                cache[(i,j)] = (dfs(i, j+2) or
                                (match and dfs(i+1, j))
                               )
                
                return cache[(i,j)]
            
            # if not starred, need to chech if we have match.
            # If yes, incr i and j by one
            # Else, no match is possible
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]

            # else did not match
            cache[(i,j)] = False
            return cache[(i,j)]
    
        # Top-down
        return dfs(i=0, j=0)
