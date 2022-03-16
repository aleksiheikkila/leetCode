""" 44. Wildcard Matching. HARD
https://leetcode.com/problems/wildcard-matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).


#### APPROACH
2D Dynamic Programming


Let dp[i][j]: take string with first i chars and pattern with first j chars.
Is that a match?

    so as we step down the rows, we make the string under consideration longer
    and when we step to right, we make the pattern under consideration longer

Update rules:
Special characters:
 - if the last pattern character is ?, we take the dp value from dp[i-1][j-1]
    (so ? consumes the last char in (sub)string under consideration...)
 - if the last pattern character is *, we take the dp value as dp[i-1][j] or dp[i][j-1]
    (so * matches to the last char(s), or * matches to zero chars)
Normal characters:
 - if the last s and last p are different, mark as False
 - if the last s and last p are same, take the value from dp[i-1][j-1]

Answer will be in dp[-1][-1].
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def rem_extra_stars(p):
            """Collapse subsequent stars to only one. 
            E.g. pattern a*****b -> a*b
            """
            new_p = ["#"]
            for char in p:
                if new_p[-1] == "*" and char == "*":
                    continue
                new_p.append(char)
            return "".join(new_p[1:])
                          
        p = rem_extra_stars(p)              
        NROWS, NCOLS = len(s)+1 , len(p)+1
                             
        dp = [[False for _ in range(NCOLS)] 
                for _ in range(NROWS)]
        
        # Initializations
        dp[0][0] = True  # empty string matches to empty pattern
        # Can empty string match to some non-empty pattern? Yes, only to '*' 
        if NCOLS > 1:
            dp[0][1] = p[0] == "*"
                                                
        # First column can be left false (except for index (0,0))

        # Loop over the 2D dp table and use update rules
        for j in range(1, NCOLS):
            for i in range(1, NROWS):
                if p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]            
                elif p[j-1] == "?" or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]                   
                else:  # case normal characters do not match:
                    dp[i][j] = False
                
        return dp[-1][-1]
